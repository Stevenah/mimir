from utils.model_utils import apply_guided_backprop
from utils.image_utils import deprocess_saliency, deprocess_gradcam, deprocess_image
from utils.file_utils import save_gradcam_image, save_guided_gradcam_image, save_saliency_image

from scipy.misc import imresize

from flask import current_app as app

from tf_extensions.activations import register_guided_relu

from keras.models import Model, load_model, model_from_json
from keras.layers.convolutional import _Conv
from keras.layers.pooling import _Pooling1D, _Pooling2D, _Pooling3D
from keras.layers import GlobalAveragePooling2D, Activation

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
    """ Wrapper class for the keras Model

        # Arguments
            classes: number of classes to classify into.
            model_file (optional): model file to load from. When
                used in in conjunction with model_weights and model_json,
                this will be prioritized.
            model_weights (optional): model weights file to load from. Must
                be passed together with model_json or will throw an exception.
                if model_file is present, this will be ignored.
            model_json (optional): model_json file to load from. Must
                be passed together with model_weights or will throw an exception.
                if model_file is present, this will be ignored.

        # Returns
            A ModelHelper instance.

    """
    def __init__(self,
        classes,
        model_file=None,
        model_weights=None,
        model_json=None):

        if model_file is None and (model_weights is None or model_json is None):
            raise Exception("Error!")

        register_guided_relu()

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
        """ Initialize models
        """
        if self.model_file is not None:
            self.model = load_model(self.model_file)
        else:
            self.model = model_from_json(open(self.model_json).read())
            self.model.load_weights(self.model_weights)

        self.guided_model = apply_guided_backprop(self.model)
        self.graph = tf.get_default_graph()

    def reset(self):
        """ Clears greaph and re-initializes models.
        """
        K.clear_session()
        self.initialize_model()

    def get_layers(self):
        """ Gets the convolutional layers of the model.

            # Returns
                A list containing the convolutional layers of the 
                model.
        """
        return [layer.name for layer in self.model.layers if isinstance(layer, _Conv)]

    def get_classes(self):
        """ Gets the classes of the model.

            # Returns
                A list containing the classes to be classified into 
                of the model.
        """
        return [self.labels[class_id] for class_id in self.labels]
            
    def labeled_predictions(self, image):
        """ Gets labeled predictions.

            # Arguments
                image: Image to be classified

            # Returns
                A dictionary containing a class-prediction pair.
        """
        predictions = self.predict(image)
        return { label: predictions[i].tolist() 
            for i, label in self.labels.items()}
                
    def prepare_image(self, image):
        """ Prepares an image for classification.

            # Arguments
                image: Image to be classified

            # Returns
                A resized image ready to be passed through
                the convolutional model.
        """
        image = imresize(image, (self.image_width, 
            self.image_height, self.image_channels))
        
        image = image.reshape(1, self.image_width, 
            self.image_height, self.image_channels)
        
        return image

    def predict(self, image, max_only=False):
        """ Classifies an image.

            # Arguments
                image: Image to be classified
                max_only (default True): Returns single in corresponding
                    to highest classification prediction.

            # Returns
                A dictionary containing class ids and predictions or 
                a single tuple containing the class id and prediction for the
                highest predicted class.
        """
        with self.graph.as_default():

            if self.image_rescale:
                image = image[...,::-1]

            if self.image_bgr:
                image = np.true_divide(image, 255.)

            if max_only:
                return np.argmax(image, axis=1)

            return self.model.predict(image)[0]

    def visualize(self, image, layer_id, class_id):
        """ Visualizes an image going through the convolutional neural network.

            # Arguments
                image: Image to be visualized for.
                layer_id: Id of the layer to be visualized for.
                class_id: Id of the class to be visualized for.

            # Returns
                gradcam: The grad-CAM representation of the given image
                    at the point of the layer_id maximized for the given
                    class_id.
                saliency: The saliency map representation of the given image
                    at the point of the layer_id.
                guided_gradcam: The guided grad-CAM representation of the given image
                    at the point of the layer_id maximized for the given
                    class_id.
        """
        image = self.prepare_image(image)
        processed = image

        if self.image_rescale:
            processed = processed[...,::-1]

        if self.image_bgr:
            processed = np.true_divide(processed, 255.)

        saliency = self.create_saliency_map(processed, layer_id)
        gradcam = self.create_gradcam(processed, class_id, layer_id)
        guided_gradcam = self.create_guided_gradcam(saliency, gradcam)

        gradcam = deprocess_gradcam(image, gradcam)
        saliency = deprocess_saliency(saliency)
        guided_gradcam = deprocess_image(guided_gradcam)

        return gradcam, saliency, guided_gradcam

    def visualize_image(self, image, image_id, layer_id, class_id):
        """ Visualizes an image going through the convolutional neural network
            and saves them to disk.

            # Arguments
                image: Image to be visualized for.
                image_id: Id of imag eto be visualized for, used when saving
                    the various representations.
                layer_id: Id of the layer to be visualized for.
                class_id: Id of the class to be visualized for.
        """
        class_id = int(class_id)

        if class_id > self.number_of_classes:
            raise Exception('Selected class not in model!')

        if layer_id not in self.layers:
            raise Exception('Selected layer not in model!')

        gradcam, saliency, guided_gradcam = self.visualize(image, layer_id, class_id)

        save_gradcam_image(gradcam, image_id, layer_id, class_id)      
        save_saliency_image(saliency, image_id, layer_id, class_id)  
        save_guided_gradcam_image(guided_gradcam, image_id, layer_id, class_id)

    def create_saliency_map(self, image, layer_id):
        """ Creates the saliency map representation of the given image
            at the point of the layer_id.

            # Arguments
                image: Image to be visualized for.
                layer_id: Id of the layer to be visualized for.
        """
        layer_output = self.guided_model.get_layer(layer_id).output

        loss = K.sum(K.max(layer_output, axis=3))
        saliency = K.gradients(loss, self.guided_model.input)[0]

        return K.function([self.guided_model.input], [saliency])([image])

    def create_gradcam(self, image, class_id, layer_id):
        """ Creates the grad-CAM representation of the given image
            at the point of the layer_id maximized for the given
            class_id.

            # Arguments
                image: Image to be visualized for.
                layer_id: Id of the layer to be visualized for.
                class_id: Id of the class to be visualized for.
        """
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
        """The guided grad-CAM representation of the given image
            by combining the grad-CAM and the saliency map.

            # Arguments
                saliency_map: saliency map of image.
                grad_cam: grad-CAM of image.
        """
        saliancy_map = np.squeeze(saliancy_map)
        grad_cam = grad_cam[..., np.newaxis]
        return saliancy_map * grad_cam