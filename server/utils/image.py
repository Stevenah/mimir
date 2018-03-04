from flask import current_app as app
from scipy.misc import imsave, imread, imresize

import keras.backend as K
import tensorflow as tf
import numpy as np
import os
import cv2
import base64

def deprocess_image(image):
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

# def prepare_image(image, width, height, channels):
#     with open(os.path.join(app.config['TEMP_DIRECTORY'], 'image.png'), 'wb') as output:
#         output.write(image)

#     image = imread(os.path.join(app.config['TEMP_DIRECTORY'], 'image.png'), mode='RGB')

#     image = imresize(image, (width, height, channels))
#     image = image.reshape(1, width, height, channels)
#     return image

def prepare_image(image, width, height, channels):
    image = imresize(image, (width, height, channels))
    image = image.reshape(1, width, height, channels)
    return image

def prepare_base64_image(image, width, height, channels):
    image = decode_base64(image)

    with open(os.path.join(app.config['TEMP_DIRECTORY'], 'image.png'), 'wb') as output:
        output.write(image)

    image = imread(os.path.join(app.config['TEMP_DIRECTORY'], 'image.png'), mode='RGB')
    
    return prepare_image(image, width, height, channels)
    
def decode_base64(data):
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += '='* (4 - missing_padding)
    return base64.b64decode(data.split(",",1)[1] )

def process_image(image, bgr=False, rescale=False):
    
    original = image
    processed = image

    if bgr:
        processed = rgb_to_bgr(processed)

    if rescale:
        processed = np.true_divide(processed, 255.)

    return original, processed

def process_base64_image(image, width, height, channel):
    image = decode_base64(image)
    image = prepare_image(image)
    return process_image(image, width, height, channel)


def rgb_to_bgr(image):
    return image[...,::-1]