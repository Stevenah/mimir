import keras.backend as K
import tensorflow as tf
import numpy as np

from keras.layers import GlobalAveragePooling2D, Activation
from scipy.misc import imresize, imread

import cv2

class KerasVisualizer():

    def saliency(self, model, image, layer_id):
        with tf.get_default_graph().gradient_override_map({'Relu': 'GuidedRelu'}):
            layer_output = model.get_layer(layer_id).output
            model_input = model.input

            loss = K.sum(K.max(layer_output, axis=3))
            saliency = K.gradients(loss, model_input)[0]

            return K.function([model_input], [saliency])([image])

    def cam(self, model, image, class_id, layer_id):
        input_layer= model.layers[0].input
        output_layer = model.layers[-1].output
        target_layer = model.get_layer(layer_id).output

        loss = K.sum(output_layer * K.one_hot([class_id], int(output_layer.shape[1])))

        gradients = K.gradients(loss, target_layer)[0]

        weights = GlobalAveragePooling2D()(gradients)
        
        cam = K.sum(weights * target_layer, axis=-1)
        cam = Activation('relu')(cam)

        gradcam_fn = K.function([input_layer], [cam])

        cam = gradcam_fn([image])
        cam = imresize(np.squeeze(cam), tuple(input_layer.shape[1:3]))

        return cam / np.max(cam)

    def guided_cam(self, model, image, class_id, layer_id):
        saliency = np.squeeze(self.saliency(model, image, layer_id))
        cam = self.cam(model, image, class_id, layer_id)

        return np.squeeze(saliency) * cam[..., np.newaxis]


def deprocess_image(image):
    """ 
        # Source
            https://github.com/keras-team/keras/blob/master/examples/conv_filter_visualization.py
    """
    if np.ndim(image) > 3:
        image = np.squeeze(image)
        
    image -= image.mean()
    image /= (image.std() + 1e-5)
    image *= 0.1

    image += 0.5
    image = np.clip(image, 0, 1)

    image *= 255
    
    image = np.clip(image, 0, 255).astype('uint8')
    return image

def deprocess_saliency(saliency, grayscale=False):
    if np.ndim(saliency) > 3:
        saliency = np.squeeze(saliency)

    saliency *= 255
    saliency = np.clip(saliency, 0, 255)
    
    if grayscale:
        saliency = cv2.cvtColor(saliency, cv2.COLOR_BGR2GRAY)

    return saliency

def deprocess_gradcam(image, gradcam, greyscale=False):
    if np.ndim(image) > 3:
        image = np.squeeze(image)

    image -= np.min(image)     
    image  = np.minimum(image, 255)

    gradcam = cv2.applyColorMap(np.uint8(255 * gradcam), cv2.COLORMAP_JET)
    gradcam = np.float32(gradcam) + np.float32(image)
    gradcam = 255 * gradcam / np.max(gradcam)

    if greyscale:
        gradcam = cv2.cvtColor(gradcam, cv2.COLOR_BGR2GRAY)

    return gradcam