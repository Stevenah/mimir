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

from blueprints.utils import save_image

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

        self.image_rescale = True
        self.image_bgr = True

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

    def prepare_base64_image(self, image):
        return prepare_base64_image(image, self.image_width, 
            self.image_height, self.image_channels)
            
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

    def predict_max(self, image):
        return np.argmax(self.predict(image))

    def save_image(self, image, image_id, filter_type, layer_id, class_id):

        image_id = self.get_image_id(image_id, filter_type, layer_id, class_id)
        file_name = f'{image_id}.jpg'

        base_dir = app.config[f'{filter_type.upper()}_DIRECTORY']
        file_dir = os.path.join(base_dir, image_id)

        if not os.path.exists(file_dir):
            os.makedirs(file_dir)

        file_path = os.path.join(file_dir, file_name)

        save_image(image, file_path, as_np=True)

    def get_image_id(self, image_id, image_filter, layer_id, class_id):
        return f'{image_id}_{image_filter}_{layer_id}_{class_id}'

    def load_layer_visualization(self, layer, category):
        return {
            'gradcam': self.load_guided_gradcam(layer, category),
            'heatmap': self.load_gradcam(layer, category)
        }

    def create_saliency_map(self, image, layer_id):
        layer_output = self.guided_model.get_layer(layer_id).output

        loss = K.sum(K.max(layer_output, axis=3))
        saliency = K.gradients(loss, self.guided_model.input)[0]

        return K.function([self.guided_model.input], [saliency])([image])

    def create_gradient_cam(self, image, class_id, layer_id):
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

    def create_guided_gradient_cam(self, saliancy_map, grad_cam):
        saliancy_map = np.squeeze(saliancy_map)
        grad_cam = grad_cam[..., np.newaxis]
        return saliancy_map * grad_cam

    def visualize_image(self, image, image_id, layer_id, class_id):

        image = self.prepare_image(image)
        gradcam, saliency, guided_gradcam = self.guided_gradcam(image, layer_id, class_id)

        self.save_image(gradcam, image_id, 'gradcam', layer_id, class_id)      
        self.save_image(saliency, image_id, 'saliency', layer_id, class_id)  
        self.save_image(guided_gradcam, image_id, 'guided_gradcam', layer_id, class_id)

    def archive(self, image, image_id, sub_dir, layer_id=None, class_id=None, save_prediction=False):

        archive_dir = app.config['ARCHIVE_DIRECTORY']
        model_dir = app.config['MODEL_NAME']
        image_dir = os.path.join(archive_dir, model_dir, image_id) 
        path = os.path.join(image_dir, sub_dir)

        if layer_id and class_id:
            filename = f'{image_id}_{layer_id}_{class_id}.jpg'
        else:
            filename = f'{image_id}.jpg'

        if not os.path.exists(path):
            os.makedirs(path)

        if save_prediction:
            predictions = self.predict(self.prepare_image(image))
            with open(os.path.join(image_dir, 'predictions.txt'), 'w') as f:
                json.dump(
                    self.labeled_predictions(image), f,
                    sort_keys=True,
                    indent=4,
                    separators=(',', ': '))

        save_image(image, os.path.join(path, filename), as_np=True)
        
    def visualize_model(self, image, image_id):

        self.archive(image, image_id, 'original')

        image = self.prepare_image(image)
        predictions = self.predict(image)

        for class_id in range(0, self.number_of_classes):
            
            if predictions[class_id] < .2:
                continue

            for layer_index, layer in enumerate(self.model.layers):
                if isinstance(layer, _Conv):

                    gradcam, saliency, guided_gradcam = self.guided_gradcam(
                        image, layer.name, class_id)
                    
                    self.archive(gradcam, image_id, 'gradcam', layer.name, class_id)      
                    self.archive(saliency, image_id, 'saliency', layer.name, class_id)  
                    self.archive(guided_gradcam, image_id, 'guided_gradcam', layer.name, class_id)

            self.reset()

    
    def guided_gradcam(self, image, layer_id, class_id):

        original, processed = self.process_image(image)
        
        saliency = self.create_saliency_map(processed, layer_id)
        gradcam = self.create_gradient_cam(processed, class_id, layer_id)
        guided_gradcam = self.create_guided_gradient_cam(saliency, gradcam)

        gradcam = deprocess_gradcam(original, gradcam)
        saliency = deprocess_saliency(saliency)
        guided_gradcam = deprocess_image(guided_gradcam)

        self.reset()

        return gradcam, saliency, guided_gradcam

    # def save_prediction_results(self, image):
    #     with open(os.path.join(self.image_dir, 'predictions.txt'), 'w') as file:
    #         file.write(json.dumps(self.labeled_predictions(image)))

    # def load_image(self, image_id, filter_type, layer_id, class_id):
    #     with open(f'{image_id}_{filter_type}_{layer_id}_{class_id}.jpg', 'rb') as f:
    #         return base64.b64encode(f.read()).decode('UTF-8')
    
    # def load_all_layer_visualizations(self, category):
    #     return {layer: self.load_layer_visualization(layer, category) 
    #         for layer in self.visualized_layers}

    # def load_all_category_visualizations(self):
    #     return {label: self.load_all_layer_visualizations(category) 
    #         for category, label in self.labels.items()}

    # def set_image_dir(self, path):
    #     os.makedirs(path)
    #     self.image_dir = path

    # def get_visualized_layers(self):
    #     return self.visualized_layers
    
    # def add_visualized_layer(self, layer_id, layer_index):
    #     if layer_id not in self.visualized_layers:
    #         self.visualized_layers[layer_id] = layer_index