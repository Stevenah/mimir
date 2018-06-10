from flask import current_app as app
from database import db
from models.Image import Image
from models.Visualization import Visualization

import os
import cv2
import base64
import shutil
import numpy as np


def initialize_directories():
    if not os.path.isdir('../model'):
        os.makedirs('../model')

    if not os.path.isdir('uploads/images'):
        os.makedirs('uploads/images')

    if not os.path.isdir('uploads/thumbnails'):
        os.makedirs('uploads/thumbnails')

    if not os.path.isdir('uploads/gradcam'):
        os.makedirs('uploads/gradcam')

    if not os.path.isdir('uploads/guided_gradcam'):
        os.makedirs('uploads/guided_gradcam')

    if not os.path.isdir('uploads/saliency'):
        os.makedirs('uploads/saliency')

    if not os.path.isdir('uploads/chunks'):
        os.makedirs('uploads/chunks')

    if not os.path.isdir('uploads/videos'):
        os.makedirs('uploads/videos')


def save_standard_file(f, file_id, file_name=None, from_type='string', file_type='image'):
    """ Saves a file to the standard directory.

        # Arguments
            f: file to be saved.
            path: path of file to be saved.
            from_type: format of file to be saved.
            file_type: type of file. Either image or video.

        # Raises
            NotImplementedError: if file_type is not supported.
    """
    if file_type == 'image':
        save_image(f, file_name)
        return
        
    if file_type == 'video':
        save_standard_video(f, file_id, file_name)
        return
        
    raise NotImplementedError(f'Support for {file_tpye} is currenlty not supported!')

def save_image(source, file_name, from_type='string'):
    """ Saves an image to disk.

        # Arguments
            source: image to be saved.
            from_type: format of image to be saved.

        # Raises
            NotImplementedError: if from_type is not supported.
    """

    image = Image()

    db.session.add(image)
    db.session.flush()

    image.name = file_name
    image.path = f'uploads/images/{image.id}_{file_name}'
    image.thumbnail = f'uploads/thumbnails/{image.id}_{file_name}'

    if from_type == 'np_array':
        cv2.imwrite(image.path, source)

    elif from_type == 'string':
        with open(image.path, 'wb+') as f:
            f.write(source.read())

    else:
        raise NotImplementedError(f'Support for {from_type} is currenlty not supported!')

    prediction, label, class_index = app.config['MODEL'].predict_from_path(image.path)

    image.label = label
    image.prediction = prediction
    image.class_index = int(class_index)

    thumbnail = cv2.imread(image.path) 
    thumbnail = cv2.resize(thumbnail, (100, 100))
    cv2.imwrite(image.thumbnail, thumbnail)

    db.session.add(image)
    db.session.commit()


def save_visualization(source, image_id, layer_id, class_id, viz_type, from_type='string'):
    """ Saves an image to disk.

        # Arguments
            source: image to be saved.
            from_type: format of image to be saved.

        # Raises
            NotImplementedError: if from_type is not supported.
    """

    image = Visualization()

    image.name = f'{layer_id}_{class_id}_{image_id}_{viz_type}.png'
    image.target_layer = layer_id
    image.target_class = class_id
    image.image_id = image_id
    image.type = viz_type
    image.path = f'uploads/{viz_type}/{image.name}_{image.id}_{image.name}'

    if from_type == 'np_array':
        cv2.imwrite(image.path, source)

    elif from_type == 'string':
        with open(image.path, 'wb+') as f:
            f.write(source.read())

    else:
        raise NotImplementedError(f'Support for {from_type} is currenlty not supported!')

    db.session.add(image)
    db.session.commit()

def load_visualization(image_id, layer_id, class_id, viz_type, as_type='string'):
    """ Load image from path.
    
        # Arguments
            path: location of image to be loaded
            as_type: load image as type, such as np array, 
            string or base 64.

        # Returns
            returns image from path.
    """

    image = Visualization.query.filter_by(image_id=image_id, target_layer=layer_id, target_class=class_id, type=viz_type).first()

    if as_type == 'np_array':
        image = cv2.imread(image.path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return image

    if as_type == 'base_64':
        with open(image.path, 'rb') as f:
            return base64.b64encode(f.read()).decode('UTF-8')

    if as_type == 'string':
        with open(image.path, 'rb') as f:
            return f.read()

    raise NotImplementedError(f'Support for {as_type} is currenlty not supported!')


def load_image(image_id, as_type='string', thumbnail=False):
    """ Load image from path.
    
        # Arguments
            path: location of image to be loaded
            as_type: load image as type, such as np array, 
            string or base 64.

        # Returns
            returns image from path.
    """

    image = Image.query.get(image_id)

    if as_type == 'np_array':
        image = cv2.imread(image.thumbnail if thumbnail else image.path)
        return image

    if as_type == 'base_64':
        with open(image.thumbnail if thumbnail else image.path, 'rb') as f:
            return base64.b64encode(f.read()).decode('UTF-8')

    if as_type == 'string':
        with open(image.thumbnail if thumbnail else image.path, 'rb') as f:
            return f.read()

    raise NotImplementedError(f'Support for {as_type} is currenlty not supported!')

def load_images(thumbnails=False):
    """ Load all images from the standard directory.
    
        # Returns
            list of images from the standard directory in base 64 format.
    """

    images = []

    for image in Image.query.all():

        images.append({
            'id': image.id,
            'label': image.label,
            'prediction': image.prediction,
            'classIndex': image.class_index,
            'source': load_image(image.id, as_type='base_64', thumbnail=thumbnails)
        })

    return images

def save_video(video, path):
    """ Save video to disk.

        # Arguments
            video: video to be saved.
            path: path for image to be saved to.
    """
    dir_path = os.path.dirname(path)

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    with open(path, 'wb+') as f:
        f.write(video.read())

def save_standard_video(video, video_id, file_name=None, from_type='string'):
    """ Save video to the standard directory.

        # Arguments
            video: video to be saved.
            video_id: uuid of video.
            file_name: name of video to be saved.
    """

    if file_name is not None:
        file_name = add_file_extension(video_id, '.mp4')

    save_video(video, os.path.join('uploads/videos', video_id, file_name))

def save_chunk(chunk, file_id, file_name, chunk_index):
    """ Save file chunk.

        # Arguments
            chunk: chunk to be saved.
            file_id: uuid of chunk of file to be saved.
            file_name: file name of chunk to be saved.
            chunk_index: index of chunk to be saved.
    """

    file_dir = os.path.join('uploads/chunks', file_id)

    if not os.path.exists(file_dir):
        os.makedirs(file_dir)

    with open(os.path.join(file_dir, chunk_index), 'wb+') as f:
        f.write(chunk.read())

def upload(f, form_attributes):
    """ Handles upload of files.

        # Arguments
            f: file to be uploaded.
            form_attributes: attributes from fine uploader.
    """
    chunked = False

    file_name = form_attributes['qqfilename']
    file_id = form_attributes['qquuid']
    file_type = get_file_type(os.path.splitext(file_name)[1])

    if 'qqtotalparts' in form_attributes:
        chunked = True
        chunk_size = int(form_attributes['qqtotalparts'])
        chunk_index = int(form_attributes['qqpartindex'])

    if chunked and chunk_size > 1:
        save_chunk(f, file_id, file_name, str(chunk_index))

    if chunked and (chunk_size - 1 == chunk_index):
        combine_chunks(file_id, chunk_size)
        video_to_images(file_id)
    
    if not chunked:
        save_standard_file(f, file_id, file_name, file_type=file_type)

def combine_chunks(file_id, chunk_size):
    """ Combines chunks from file

        # Arguments
            chunk_dir: directory of chunks.
            file_path: path of file where chunks should be 
                combined to.
            chunk_size: number of chunks in file is split into.
    """
    file_path = os.path.join('uploads/videos', file_id)
    chunk_dir = os.path.join('uploads/chunks', file_id)

    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))

    with open(file_path, 'wb+') as f:
        for chunk_index in range(chunk_size):
            chunk = os.path.join(chunk_dir, str(chunk_index))
            with open(chunk, 'rb') as source:
                f.write(source.read())

    shutil.rmtree(chunk_dir)

def get_file_type(file_extension):
    """ Gets file type, either image or video.

        # Arguments
            file_extension: file extension to get 
            file type of.
    """
    image_extensions = [
        '.jpg', '.jpeg'
    ]

    video_extensions = [
        '.avi', '.mp4'
    ]

    if file_extension in image_extensions:
        return 'image'

    if file_extension in video_extensions:
        return 'video'
        
def add_file_extension(file_name, extension):
    """ Add file extension to file name.

        # Returns
            file name with added file extension.
    """
    if extension[0] == '.':
        return f'{file_name}{extension}'
    return f'{file_name}.{extension}'

def video_to_images(video_id):
    """ Converts video to frames and saves to disk.

        # Arguments
            file_path: path to video file.
            video_id: uuid of video.
    """
    video = cv2.VideoCapture(f'uploads/videos/{video_id}')

    print("Processing video to frames...")

    while True:
        ret, frame = video.read()

        if not ret:
            break

        frame_id = f'{video_id}-{video.get(cv2.CAP_PROP_POS_MSEC)}'
        file_name = add_file_extension(frame_id, '.jpg')

        save_image(frame, file_name, 'np_array')
