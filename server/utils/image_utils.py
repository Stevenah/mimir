from flask import current_app as app

import keras.backend as K
import tensorflow as tf
import numpy as np
import os
import cv2
import base64

def deprocess_image(image):
    """ Deprocess image

        # Source
            https://github.com/keras-team/keras/blob/master/examples/conv_filter_visualization.py

        # Returns
            deprocessed image.
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
    """ Deprocess saliency map.

        # Arguments
            saliency: saliency map representation of image
            greyscale (optional): whether or not to 
            greyscale imag

        # Returns
            deprocessed saliency map
    """
    if np.ndim(saliency) > 3:
        saliency = np.squeeze(saliency)

    saliency *= 255
    saliency = np.clip(saliency, 0, 255)
    
    if grayscale:
        saliency = cv2.cvtColor(saliency, cv2.COLOR_BGR2GRAY)

    return saliency

def deprocess_gradcam(image, gradcam, greyscale=False):
    """ Deprocess grad-CAM.

        # Arguments
            image: original image.
            gradcam: grad-CAM representation of image
            greyscale (optional): whether or not to 
            greyscale image.

        # Returns
            deprocessed grad-CAM
    """
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