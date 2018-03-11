from keras.models import model_from_json, load_model
from utils.util import temppath

import tensorflow as tf
import os

def clone(model):
    """ Clonse model.

        # Arguments
            model: model to be cloned.
        
        # Returns
            Cloned model.

    """
    temp_path = temppath('temp_model')
    model.save(temp_path)
    model_clone = load_model(temp_path)
    os.remove(temp_path)
    return model_clone

def apply_guided_backprop(model):
    """ Applied guided backprop relu to model.

        # Arguments
            model: model to be changed.

        # Returns
            modified model.
    """
    with tf.get_default_graph().gradient_override_map({'Relu': 'GuidedRelu'}):

        modified_model = clone(model)

        for layer in model.layers[1:]:
            if hasattr(layer, 'activation'):
                layer.activation = tf.nn.relu
        
        return modified_model