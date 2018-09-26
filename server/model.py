from keras.models import load_model

from scipy.misc import imresize, imread

import keras.backend as K
import tensorflow as tf
import numpy as np

import os

class KerasNeuralNet():

    def __init__(self, model, class_labels, image_processor=None, **kwargs):
        self.model = model
        self.class_labels = class_labels
        self.image_processor = image_processor        
        self.graph = tf.get_default_graph()

    def predict(self, image, with_labels=False):
        image = self.image_processor.process(image)
        with self.graph.as_default():
            return self.model.predict(image)[0]

    def load_model(self, model_config, class_labels):
        self.model = load_model(model_config)
        self.class_labels = class_labels

class ImagePreprocessor():

    def __init__(self, image_width, image_height, 
        image_channels, rescale=None, bgr=False):

        self.image_width = image_width
        self.image_height = image_height
        self.image_channels = image_channels

        self.rescale = rescale
        self.bgr = bgr

    def process(self, image):

        image = imresize(image, (self.image_width, 
            self.image_height, self.image_channels))

        if self.rescale is not None:
            image = np.true_divide(image, 255.)

        if self.bgr:
            image = image[...,::-1]

        return image