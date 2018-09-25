from utils.model_utils import apply_guided_backprop
from utils.image_utils import deprocess_saliency, deprocess_gradcam, deprocess_image
from utils.file_utils import save_visualization

from scipy.misc import imresize

from flask import current_app as app


from models.Architecture import Architecture

from keras.models import Model, load_model, model_from_json
from keras.layers.convolutional import _Conv
from keras.layers.pooling import _Pooling1D, _Pooling2D, _Pooling3D
from keras.layers import GlobalAveragePooling2D, Activation

import keras.backend as K
import tensorflow as tf
import numpy as np

import contextlib
import tempfile
import h5py
import os
import cv2
import json
import io

class KerasVisualizer():

    def __init__(self):
        pass


class ImagePreprocessor():

    def __init__(self, image_width, image_height, 
        image_channels, rescale=None, bgr=False):

        self.image_width = image_width
        self.image_height = image_height
        self.image_channels = image_channels

        self.rescale = rescale
        self.bgr = bgr

    def load(self, path):
        return imread(path)

    def process(self, image):

        image = imresize(image, (self.image_width, 
            self.image_height, self.image_channels))

        if self.rescale is not None:
            image = np.true_divide(image, 255.)

        if self.bgr:
            image = image[...,::-1]

        return image

class ConvolutionalNeuralNetwork():

    def __init__(self, model, class_labels, image_processor=None):

        self.number_of_classes = len(class_labels)

        self.model = model
        self.class_labels = class_labels
        self.image_processor = image_processor

class KerasModel(ConvolutionalNeuralNetwork):

    def __init__(self, model, class_labels,
        image_processor=None, **kwargs):
        
        super(KerasModel, self).__init__(**kwargs)

        K.set_learning_phase(0)
        self.graph = tf.get_default_graph()
    
    def reload(self):
        K.clear_session()

    def predict(self, image, with_labels=False):
        if isinstance(image, str):
            image = self.image_processor.load(image)
        image = self.image_processor.process(image)
        with self.graph.as_default():
            return self.model.predict(image)[0]         

    def decode_predictions(self, predictions):
        return {
            self.class_labels[class_index]: prediction 
            for class_index, prediction in enumerate(predictions)
        }

    def clone(self):
        temp_path = os.path.join(tempfile.gettempdir(), 'temp_model')
        self.model.save(temp_path)
        model_clone = load_model(temp_path)
        os.remove(temp_path)
        return model_clone


class ModelManager():

    def __init__(self):
        pass

    @property
    def active(self):
        pass

    @property.setter
    def active(self, model_id):
        pass






def apply_guided_backprop(model):
    with tf.get_default_graph().gradient_override_map({'Relu': 'GuidedRelu'}):

        modified_model = clone(model)

        for layer in model.layers[1:]:
            if hasattr(layer, 'activation'):
                layer.activation = tf.nn.relu
        
        return modified_model



class ModelHelper():

    def initialize_model(self):        
        self.guided_model = apply_guided_backprop(self.model)
        self.graph = tf.get_default_graph()

    def visualize(self, image, layer_id, class_id):
        image = self.prepare_image(image)
        processed = image

        if self.image_rescale:
            processed = np.true_divide(processed, 255.)

        if self.image_bgr:
            processed = processed[...,::-1]

        saliency = self.create_saliency_map(processed, layer_id)
        gradcam = self.create_gradcam(processed, class_id, layer_id)
        guided_gradcam = self.create_guided_gradcam(saliency, gradcam)

        gradcam = deprocess_gradcam(image, gradcam)
        saliency = deprocess_saliency(saliency)
        guided_gradcam = deprocess_image(guided_gradcam)

        return gradcam, saliency, guided_gradcam

    def visualize_image(self, image, image_id, layer_id, class_id):
        class_id = int(class_id)

        if class_id > self.number_of_classes:
            raise Exception('Selected class not in model!')

        if layer_id not in self.layers:
            print(layer_id)
            print(self.layers)
            raise Exception('Selected layer not in model!')

        gradcam, saliency, guided_gradcam = self.visualize(image, layer_id, class_id)

        save_visualization(gradcam, image_id, layer_id, class_id, 'gradcam', 'np_array')      
        save_visualization(saliency, image_id, layer_id, class_id, 'saliency', 'np_array')  
        save_visualization(guided_gradcam, image_id, layer_id, class_id, 'guided_gradcam', 'np_array')

    def create_saliency_map(self, image, layer_id):
        layer_output = self.guided_model.get_layer(layer_id).output

        loss = K.sum(K.max(layer_output, axis=3))
        saliency = K.gradients(loss, self.guided_model.input)[0]

        return K.function([self.guided_model.input], [saliency])([image])

    def create_gradcam(self, image, class_id, layer_id):
        input_layer  = self.model.layers[0].input
        output_layer = self.model.layers[-1].output
        target_layer = self.model.get_layer(layer_id).output

        loss = K.sum(output_layer * K.one_hot([class_id], self.number_of_classes))

        gradients = K.gradients(loss, target_layer)[0]

        weights = GlobalAveragePooling2D()(gradients)
        
        gradcam = K.sum(weights * target_layer, axis=-1)
        gradcam = Activation('relu')(gradcam)

        gradcam_fn = K.function([input_layer], [gradcam])

        gradcam = gradcam_fn([image])
        gradcam = cv2.resize(np.squeeze(gradcam), tuple(input_layer.shape[1:3]))

        return gradcam / np.max(gradcam)

    def create_guided_gradcam(self, saliancy_map, grad_cam):
        saliancy_map = np.squeeze(saliancy_map)
        grad_cam = grad_cam[..., np.newaxis]
        return saliancy_map * grad_cam