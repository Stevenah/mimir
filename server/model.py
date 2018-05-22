from utils.model_utils import apply_guided_backprop
from utils.image_utils import deprocess_saliency, deprocess_gradcam, deprocess_image
from utils.file_utils import save_visualization

from scipy.misc import imresize

from flask import current_app as app

from tf_extensions.activations import register_guided_relu

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

class ModelHelper():
    """ Wrapper class for the keras Model

        # Returns
            A ModelHelper instance.

    """
    def __init__(self):

        K.set_learning_phase(0)

        register_guided_relu()

        self.model_file = '/tmp/model.h5'
        self.class_file = '/tmp/class.json'

        self.initialize_model()

        self.image_rescale = True
        self.image_bgr = False

    def swap_model(self, model_id):

        model = Architecture.query.with_entities(Architecture.model_file, Architecture.class_file).filter_by(id = model_id).first()

        with open(f'/tmp/model.h5', 'wb') as f:
            f.write(model.model_file)

        with open(f'/tmp/class.json', 'wb') as f:
            f.write(model.class_file)

        self.model_id = model_id
        self.initialize_model()

    def get_model_id(self):
        return self.model_id

    def initialize_model(self):
        """ Initialize models
        """
        
        self.model = load_model(self.model_file)

        self.model_id = 5

        self.image_width = self.model.input_shape[1]
        self.image_height = self.model.input_shape[2]
        self.image_channels = self.model.input_shape[3]

        self.labels = {int(k): v for k, v in json.load(open(self.class_file)).items()}
        self.number_of_classes = len(self.labels)

        self.layers = self.get_layers()
        
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
        return {class_id: self.labels[class_id] for class_id in self.labels}
            
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

    def predict_from_path(self, path):

        image = cv2.imread(path)
        image = self.prepare_image(image)

        prediction = self.predict(image)

        label = self.labels[np.argmax(prediction)]
        prob = prediction[np.argmax(prediction)]

        return prob, label, np.argmax(prediction)

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

            if self.image_bgr:
                image = image[...,::-1]

            if self.image_rescale:
                image = np.true_divide(image, 255.)

            if max_only:
                return np.argmax(self.model.predict(image)[0], axis=1)

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
            print(layer_id)
            print(self.layers)
            raise Exception('Selected layer not in model!')

        gradcam, saliency, guided_gradcam = self.visualize(image, layer_id, class_id)

        save_visualization(gradcam, image_id, layer_id, class_id, 'gradcam', 'np_array')      
        save_visualization(saliency, image_id, layer_id, class_id, 'saliency', 'np_array')  
        save_visualization(guided_gradcam, image_id, layer_id, class_id, 'guided_gradcam', 'np_array')

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
        # gradients /= (K.sqrt(K.mean(K.square(gradients))) + K.epsilon())

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