from keras.models import load_model
from keras.layers import GlobalAveragePooling2D, Activation

from scipy.misc import imresize, imread

import keras.backend as K
import tensorflow as tf
import numpy as np

import os

class ModelHelper():

    def __init__(self, model, class_labels, image_processor=None):

        K.clear_session()
        K.set_learning_phase(0)
        
        self.model = model
        self.class_labels = class_labels
        self.image_processor = image_processor
        self.graph = tf.get_default_graph()

    def predict(self, image, with_labels=False):
        with self.graph.as_default():
            return self.model.predict(
                self.image_processor.process(image)
            )[0]
    
    def saliency(self, image, layer_id):
        with tf.get_default_graph().gradient_override_map({'Relu': 'GuidedRelu'}):
            
            layer_output = model.get_layer(layer_id).output
            model_input = model.input

            loss = K.sum(K.max(layer_output, axis=3))
            saliency = K.gradients(loss, model_input)[0]

            return K.function([model_input], [saliency])([image])

    def cam(self, image, class_id, layer_id):

        input_layer= model.layers[0].input
        output_layer = model.layers[-1].output
        target_layer = model.get_layer(layer_id).output

        loss = K.sum(output_layer * K.one_hot([class_id], int(output_layer.shape[1])))

        gradients = K.gradients(loss, target_layer)[0]

        weights = GlobalAveragePooling2D()(gradients)
        
        cam = K.sum(weights * target_layer, axis=-1)
        cam = Activation('relu')(cam)

        gradcam_fn = K.function([input_layer], [cam])

        cam = gradcam_fn([image])
        cam = imresize(np.squeeze(cam), tuple(input_layer.shape[1:3]))

        return cam / np.max(cam)

    def guided_cam(self, image, class_id, layer_id):
        saliency = np.squeeze(self.saliency(model, image, layer_id))
        cam = self.cam(model, image, class_id, layer_id)

        return np.squeeze(saliency) * cam[..., np.newaxis]