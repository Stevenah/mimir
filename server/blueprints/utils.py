from flask import current_app as app

import base64
import uuid
import cv2
from scipy.misc import imsave, imread, imresize
import os
import base64

def save_file(f, path, from_type='string', file_type='image'):

    if file_type == 'image':
        save_image(f, path, 'string')
        return

    if file_type == 'video':
        save_video(f, path, 'string')
        return

    raise NotImplementedError(f'Support for {file_tpye} is currenlty not supported!')


def save_standard_file(f, image_id, file_name=None, from_type='string', file_type='image'):

    if file_type == 'image':
        save_standard_image(f, image_id, file_name)
        return

    raise NotImplementedError(f'Support for {file_tpye} is currenlty not supported!')

def save_image(image, path, from_type='string'):

    dir_path = os.path.dirname(path)

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    if from_type == 'np_array':
        cv2.imwrite(path, image)
        return

    if from_type == 'string':
        with open(path, 'wb+') as f:
            f.write(image.read())
        return

    raise NotImplementedError(f'Support for {from_type} is currenlty not supported!')

def save_standard_image(image, image_id, file_name=None, from_type='string'):
    base_dir = app.config['STANDARD_IMAGE_DIRECTORY']

    if file_name is not None:
        file_name= f'{image_id}.jpg'

    path = os.path.join(base_dir, image_id, file_name)
    save_image(image, path, from_type)

def save_gradcam_image(image, image_id, layer_id, class_id, from_type='np_array'):
    base_dir = app.config['GRADCAM_IMAGE_DIRECTORY']
    image_id = f'{image_id}-{layer_id}-{class_id}'
    file_name = f'{image_id}.jpg'
    path = os.path.join(base_dir, image_id, file_name)
    save_image(image, path, from_type)

def save_saliency_image(image, image_id, layer_id, class_id, from_type='np_array'):
    base_dir = app.config['SALIENCY_IMAGE_DIRECTORY']
    image_id = f'{image_id}-{layer_id}-{class_id}'
    file_name = f'{image_id}.jpg'
    path = os.path.join(base_dir, image_id, file_name)
    save_image(image, path, from_type)

def save_guided_gradcam_image(image, image_id, layer_id, class_id, from_type='np_array'):
    base_dir = app.config['GUIDED_GRADCAM_IMAGE_DIRECTORY']
    image_id = f'{image_id}-{layer_id}-{class_id}'
    file_name = f'{image_id}.jpg'
    path = os.path.join(base_dir, image_id, file_name)
    save_image(image, path, from_type)



def load_image(path, as_type='string'):

    if as_type == 'np_array':
        image = cv2.imread(path) 
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return image

    if as_type == 'base_64':
        with open(path, 'rb') as f:
            return base64.b64encode(f.read()).decode('UTF-8')
    
    if as_type == 'string':
        with open(path, 'rb') as f:
            return f.read()

    raise NotImplementedError(f'Support for {as_type} is currenlty not supported!')

def load_images():
    
    dir_path = app.config['STANDARD_IMAGE_DIRECTORY']
    images = []

    for image_id in os.listdir(dir_path):
        images.append({
            'id': image_id,
            'source': load_image(get_image_path(dir_path, image_id), as_type='base_64')
        })

    return images

def load_standard_image(image_id, as_type='string'):
    base_dir = app.config['STANDARD_IMAGE_DIRECTORY']
    return load_image(get_image_path(base_dir, image_id), as_type)

def load_gradcam_image(image_id, layer_id, class_id, as_type='string'):
    base_dir = app.config['GRADCAM_IMAGE_DIRECTORY']
    image_id = f'{image_id}-{layer_id}-{class_id}'
    return load_image(get_image_path(base_dir, image_id), as_type)

def load_guided_gradcam_image(image_id, layer_id, class_id, as_type='string'):
    base_dir = app.config['GUIDED_GRADCAM_IMAGE_DIRECTORY']
    image_id = f'{image_id}-{layer_id}-{class_id}'
    return load_image(get_image_path(base_dir, image_id), as_type)

def get_image_path(base_dir, image_id):
    dir_path = os.path.join(base_dir, image_id)
    file_name = os.listdir(dir_path)[0]
    return os.path.join(dir_path, file_name)


def save_video():
    pass

def load_video():
    pass

def load_videos():
    pass

def upload(f, form_attributes, file_type='image'):

    chunked = False
    chunksize = None
    chunkindex = None
    chunkdir = None

    if 'qqtotalparts' in form_attributes:
        chunked = True
        chunksize = int(form_attributes['qqtotalparts'])
        chunkindex = int(form_attributes['qqpartindex'])
        chunkdir = app.config['CHUNKS_DIRECTORY']

    file_path = ''

    file_name = form_attributes['qqfilename']
    file_uuid = form_attributes['qquuid']
    file_dir = app.config['ORIGINAL_DIRECTORY']

    path = os.path.join(file_dir, file_uuid, file_name)

    if chunked and chunksize > 1:
        path = os.path.join(chunkdir, file_uuid, file_name, str(chunkindex))

    save_standard_file(f, file_uuid, file_name, file_type)

    if chunked and (chunksize - 1 == chunkindex):

        file_path = os.path.join(file_dir, file_uuid, file_name)

        combine_chunks(
            chunksize=chunksize,
            source_dir=os.path.dirname(path),
            path=file_path)

        shutil.rmtree(os.path.dirname(os.path.dirname(path)))
    
    return file_path

def combine_chunks(chunksize, source_dir, path):

    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))

    with open(dest, 'wb+') as destination:
        for chunk_index in range(chunksize):
            chunk = os.path.join(source_dir, str(chunk_index))
            with open(chunk, 'rb') as source:
                destination.write(source.read())