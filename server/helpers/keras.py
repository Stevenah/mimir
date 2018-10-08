from keras.models import load_model
from keras.layers import GlobalAveragePooling2D, Activation

from scipy.misc import imresize, imread, imsave
from helpers.image import *

from mimir_visualizer.visualize import *

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

    def class_activation_map(self, image, class_index, layer_name);
        return generate_gradcam(self.model, image,
            class_index=class_index, layer_name=layer_name)

    def class_saliency_map(self):
        return generate_saliency(self.model, image, layer_name=layer_name)
    
    def saliency_map(self):
        return generate_class_saliency(self.model, image,
            class_index=class_index, layer_name=layer_name)