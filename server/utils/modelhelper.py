from utils.model import build as build_model, apply_guided_backprop
from utils.image import deprocess_image, prepare_base64_image, process_image
from utils.image import deprocess_saliency, deprocess_gradcam, prepare_image
from scipy.misc import imsave, imread, imresize

from flask import current_app as app

from tf_extensions.activations import register_activation_extensions

from keras.models import Model, load_model, model_from_json
from keras.layers.convolutional import _Conv
from keras.layers.pooling import _Pooling1D, _Pooling2D, _Pooling3D
from keras.layers import GlobalAveragePooling2D, Activation

from blueprints.utils import save_image, save_gradcam_image, save_guided_gradcam_image, save_saliency_image

import keras.backend as K
import tensorflow as tf
import numpy as np

import os
import cv2
import json
import base64
import uuid
import json

class ModelHelper():

    def __init__(self, classes, model_file=None, model_weights=None, model_json=None):

        if model_file is None and (model_weights is None or model_json is None):
            raise Exception("Error!")

        register_activation_extensions()

        self.model_file = model_file
        self.model_json = model_json
        self.model_weights = model_weights

        self.initialize_model()

        self.number_of_classes = len(classes)
        self.labels = classes

        self.layers = self.get_layers()
        self.visualized_layers = {}
        self.cache = {}

        self.image_width = self.model.input_shape[1]
        self.image_height = self.model.input_shape[2]
        self.image_channels = self.model.input_shape[3]

        self.image_rescale = False
        self.image_bgr = False

    def initialize_model(self):
        if self.model_file is not None:
            self.model = load_model(self.model_file)
        else:
            self.model = model_from_json(open(self.model_json).read())
            self.model.load_weights(self.model_weights)

        self.guided_model = apply_guided_backprop(self.model)
        self.graph = tf.get_default_graph()

    def reset(self):
        K.clear_session()
        self.initialize_model()

    def get_layers(self):
        return [layer.name for layer in self.model.layers if isinstance(layer, _Conv)]

    def get_classes(self):
        return [self.labels[class_id] for class_id in self.labels]
            
    def prepare_image(self, image):
        return prepare_image(image, self.image_width, 
            self.image_height, self.image_channels)

    def process_image(self, image):
        return process_image(image, self.image_rescale, self.image_bgr)

    def predict(self, image):
        with self.graph.as_default():
            _, image = self.process_image(image)
            return self.model.predict(image)[0]

    def labeled_predictions(self, image, threshold=0):
        predictions = self.predict(image)
        return {label: predictions[i].tolist() 
            for i, label in self.labels.items() if predictions[i] > threshold}

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
        gradients /= (K.sqrt(K.mean(K.square(gradients))) + K.epsilon())

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

    def visualize(self, image, layer_id, class_id):

        original, processed = self.process_image(image)
        
        saliency = self.create_saliency_map(processed, layer_id)
        gradcam = self.create_gradcam(processed, class_id, layer_id)
        guided_gradcam = self.create_guided_gradcam(saliency, gradcam)

        gradcam = deprocess_gradcam(original, gradcam)
        saliency = deprocess_saliency(saliency)
        guided_gradcam = deprocess_image(guided_gradcam)

        self.reset()

        return gradcam, saliency, guided_gradcam

    def visualize_image(self, image, image_id, layer_id, class_id):

        class_id = int(class_id)

        image = self.prepare_image(image)
        gradcam, saliency, guided_gradcam = self.visualize(image, layer_id, class_id)

        save_gradcam_image(gradcam, image_id, layer_id, class_id)      
        save_saliency_image(saliency, image_id, layer_id, class_id)  
        save_guided_gradcam_image(guided_gradcam, image_id, layer_id, class_id)