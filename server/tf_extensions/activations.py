from tensorflow.python.framework import ops
from tensorflow.python.ops import gen_nn_ops
import tensorflow as tf

def register_guided_relu():
    """ Register guided relu in tensorflow.
        
        # Source
            https://pythonexample.com/code/guided%20backprop/
            
    """
    if "GuidedRelu" not in ops._gradient_registry._registry:
        @ops.RegisterGradient("GuidedRelu")
        def _GuidedRelu(op, grad):
            dtype = op.inputs[0].dtype
            return grad * tf.cast(grad > 0., dtype) * \
                tf.cast(op.inputs[0] > 0., dtype)

def apply_guided_backprop(model):
    with tf.get_default_graph().gradient_override_map({'Relu': 'GuidedRelu'}):

        modified_model = clone(model)

        for layer in model.layers[1:]:
            if hasattr(layer, 'activation'):
                layer.activation = tf.nn.relu
        
        return modified_model