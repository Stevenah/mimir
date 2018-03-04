from keras.models import model_from_json, load_model
from utils.util import temppath

import tensorflow as tf
import os

def build(model_json, model_weigths):
    try:
        model = model_from_json(open(model_json).read())
        model.load_weights(model_weigths)
        return model
    except Exception:
        raise Exception('Failed to load model/weights')

def clone(model):
    temp_path = temppath('temp_model')
    model.save(temp_path)
    model_clone = load_model(temp_path)
    os.remove(temp_path)
    return model_clone

def apply_guided_backprop(model):
    with tf.get_default_graph().gradient_override_map({'Relu': 'GuidedRelu'}):

        modified_model = clone(model)

        for layer in model.layers[1:]:
            if hasattr(layer, 'activation'):
                layer.activation = tf.nn.relu
        
        return modified_model