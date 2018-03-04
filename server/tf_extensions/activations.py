from tensorflow.python.framework import ops
import tensorflow as tf

def register_guided_relu():
    if "GuidedRelu" not in ops._gradient_registry._registry:
        @ops.RegisterGradient("GuidedRelu")
        def _GuidedRelu(op, grad):
            dtype = op.inputs[0].dtype
            gate_g = tf.cast(grad > 0., dtype)
            gate_y = tf.cast(op.inputs[0] > 0., dtype)
            return grad * gate_g * gate_y

def register_activation_extensions():
    register_guided_relu()