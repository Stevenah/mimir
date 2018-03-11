from flask import current_app as app

import os
import cv2
import base64
import shutil
import numpy as np

def save_file(f, path, from_type='string', file_type='image'):
    """ Saves a file to disk.

        # Arguments
            f: file to be saved.
            path: path of file to be saved.
            from_type: format of file to be saved.
            file_type: type of file. Either image, video 
                or chunk.

        # Raises
            NotImplementedError: if file_type is not supported.
    """
    if file_type == 'image':
        save_image(f, path, 'string')
        return

    if file_type == 'video':
        save_video(f, path, 'string')
        return

    if file_type == 'chunk':
        save_chunk(f, path, 'string')
        return
        
    raise NotImplementedError(f'Support for {file_tpye} is currenlty not supported!')

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
        save_standard_image(f, file_id, file_name)
        return
        
    if file_type == 'video':
        save_standard_video(f, file_id, file_name)
        return
        
    raise NotImplementedError(f'Support for {file_tpye} is currenlty not supported!')

def save_image(image, path, from_type='string'):
    """ Saves an image to disk.

        # Arguments
            image: image to be saved.
            path: path of image to be saved.
            from_type: format of image to be saved.

        # Raises
            NotImplementedError: if from_type is not supported.
    """
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
    """ Saves an image to the standard directory.

        # Arguments
            image: image to be saved.
            image_id: uuid of the image
            file_name: name of file.
            from_type: format of image to be saved.
    """
    base_dir = app.config['STANDARD_IMAGE_DIRECTORY']

    if file_name is not None:
        file_name = add_file_extension(image_id, '.jpg')

    file_path = os.path.join(base_dir, image_id, file_name)
    
    # save_thumbnail(image, file_id, file_name, from_type)
    save_image(image, file_path, from_type)

def save_thumbnail(image, image_id, file_name, from_type):
    """ Saves an image to the thumbnail directory.

        # Arguments
            image: image to be saved.
            image_id: uuid of the image
            file_name: name of file.
            from_type: format of image to be saved.
    """
    thumbnail_dir = app.config['STANDARD_THUMBNAIL_DIRECTORY']

    if from_type == 'string':
        image = np.fromstring(image)

    image = cv2.resize(image, (100, 100))

    file_path = os.path.join(thumbnail_dir, image_id, file_name)
    save_image(image, file_path, from_type='np_array')

def save_gradcam_image(image, image_id, layer_id, class_id, from_type='np_array'):
    """ Saves an image to the gradcam directory.

        # Arguments
            image: image to be saved.
            image_id: uuid of the image
            layer_id: id of layer grad-CAM is visualized for.
            class_id: id of class grad-CAM is visualized for.
            from_type: format of image to be saved.
    """
    base_dir = app.config['GRADCAM_IMAGE_DIRECTORY']
    image_id = get_cam_file_name(image_id, layer_id, class_id)
    file_name = add_file_extension(image_id, '.jpg')
    path = os.path.join(base_dir, image_id, file_name)
    save_image(image, path, from_type)

def save_saliency_image(image, image_id, layer_id, class_id, from_type='np_array'):
    """ Saves an image to the saliency directory.

        # Arguments
            image: image to be saved.
            image_id: uuid of the image
            layer_id: id of layer grad-CAM is visualized for.
            class_id: id of class grad-CAM is visualized for.
            from_type: format of image to be saved.
    """
    base_dir = app.config['SALIENCY_IMAGE_DIRECTORY']
    image_id = get_cam_file_name(image_id, layer_id, class_id)
    file_name = add_file_extension(image_id, '.jpg')
    path = os.path.join(base_dir, image_id, file_name)
    save_image(image, path, from_type)

def save_guided_gradcam_image(image, image_id, layer_id, class_id, from_type='np_array'):
    """ Saves an image to the guided gradcam directory.

        # Arguments
            image: image to be saved.
            image_id: uuid of the image
            layer_id: id of layer grad-CAM is visualized for.
            class_id: id of class grad-CAM is visualized for.
            from_type: format of image to be saved.
    """
    base_dir = app.config['GUIDED_GRADCAM_IMAGE_DIRECTORY']
    image_id = get_cam_file_name(image_id, layer_id, class_id)
    file_name = add_file_extension(image_id, '.jpg')
    path = os.path.join(base_dir, image_id, file_name)
    save_image(image, path, from_type)

def load_image(path, as_type='string'):
    """ Load image from path.
    
        # Arguments
            path: location of image to be loaded
            as_type: load image as type, such as np array, 
            string or base 64.

        # Returns
            returns image from path.
    """
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
    """ Load all images from the standard directory.
    
        # Returns
            list of images from the standard directory in base 64 format.
    """
    dir_path = app.config['STANDARD_IMAGE_DIRECTORY']
    images = []

    for image_id in os.listdir(dir_path):
        images.append({
            'id': image_id,
            'source': load_image(get_image_path(dir_path, image_id), as_type='base_64')
        })

    return images

def load_standard_image(image_id, as_type='string'):
    """ Load image from the standard directory.

        # Arguments
            image_id: id of image to be loaded.
            as_type: load image as type, such as np array, 
            string or base 64.

        # Returns
            image in format specified in as_type argument.
    """
    base_dir = app.config['STANDARD_IMAGE_DIRECTORY']
    return load_image(get_image_path(base_dir, image_id), as_type)

def load_gradcam_image(image_id, layer_id, class_id, as_type='string'):
    """ Load image from the standard directory.

        # Arguments
            image_id: uuid of the image to be loaded.
            layer_id: id of layer grad-CAM is visualized for.
            class_id: id of class grad-CAM is visualized for.
            as_type: load image as type, such as np array, 
            string or base 64.

        # Returns
            image in format specified in as_type argument.
    """
    base_dir = app.config['GRADCAM_IMAGE_DIRECTORY']
    image_id = get_cam_file_name(image_id, layer_id, class_id)
    return load_image(get_image_path(base_dir, image_id), as_type)

def load_guided_gradcam_image(image_id, layer_id, class_id, as_type='string'):
    """ Load image from the guided gradcam directory.

        # Arguments
            image_id: uuid of the image to be loaded.
            layer_id: id of layer grad-CAM is visualized for.
            class_id: id of class grad-CAM is visualized for.
            as_type: load image as type, such as np array, 
            string or base 64.

        # Returns
            image in format specified in as_type argument.
    """
    base_dir = app.config['GUIDED_GRADCAM_IMAGE_DIRECTORY']
    image_id = get_cam_file_name(image_id, layer_id, class_id)
    return load_image(get_image_path(base_dir, image_id), as_type)

def get_image_path(base_dir, image_id):
    """ Get image file path.

        # Arguments
            base_dir: directory to load image from.
            image_id: uuid of the image to be loaded.

        # Returns
            path to image
    """
    dir_path = os.path.join(base_dir, image_id)
    file_name = os.listdir(dir_path)[0]
    return os.path.join(dir_path, file_name)

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
    base_dir = app.config['STANDARD_VIDEO_DIRECTORY']

    if file_name is not None:
        file_name = add_file_extension(video_id, '.mp4')

    save_video(video, os.path.join(base_dir, video_id, file_name))

def save_chunk(chunk, file_id, file_name, chunk_index):
    """ Save file chunk.

        # Arguments
            chunk: chunk to be saved.
            file_id: uuid of chunk of file to be saved.
            file_name: file name of chunk to be saved.
            chunk_index: index of chunk to be saved.
    """
    base_dir = app.config['CHUNKS_DIRECTORY']
    file_dir = os.path.join(base_dir, file_id, file_name)

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
        chunk_dir = get_file_path(file_id, file_name, 'chunk')
        file_path = get_file_path(file_id, file_name, file_type)
        combine_chunks(chunk_dir, file_path, chunk_size)

        video_to_images(file_path, file_id)

        shutil.rmtree(chunk_dir)
    
    if not chunked:
        save_standard_file(f, file_id, file_name, file_type=file_type)

        # if file_type == 'video':
        #     video_to_images(get_file_path(file_id, file_name, file_type), file_id)

def combine_chunks(chunk_dir, file_path, chunk_size):
    """ Combines chunks from file

        # Arguments
            chunk_dir: directory of chunks.
            file_path: path of file where chunks should be 
                combined to.
            chunk_size: number of chunks in file is split into.
    """
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))

    with open(file_path, 'wb+') as f:
        for chunk_index in range(chunk_size):
            chunk = os.path.join(chunk_dir, str(chunk_index))
            with open(chunk, 'rb') as source:
                f.write(source.read())


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

def get_file_path(file_id, file_name, file_type, chunk_id=None):
    """ Get file path.

        # Arguments
            file_id: uuid of file.
            file_name: name of file.
            file_type: type of file
            chunk_id (optional):

        # Returns
            returns path of file.
    """
    if file_type == 'image':
        base_dir = app.config['STANDARD_IMAGE_DIRECTORY']

    if file_type == 'video':
        base_dir = app.config['STANDARD_VIDEO_DIRECTORY']

    if file_type == 'chunk':
        base_dir = app.config['CHUNKS_DIRECTORY']

    if chunk_id is not None:
        return os.path.join(base_dir, file_id, file_name, chunk_id)

    return os.path.join(base_dir, file_id, file_name)

def get_cam_file_name(file_id, layer_id, class_id):
    """ Gets file name of image representations.

        # Returns
            file name of cam representation.
    """
    return f'{file_id}-{layer_id}-{class_id}'

def add_file_extension(file_name, extension):
    """ Add file extension to file name.

        # Returns
            file name with added file extension.
    """
    if extension[0] == '.':
        return f'{file_name}{extension}'
    return f'{file_name}.{extension}'

def video_to_images(file_path, video_id):
    """ Converts video to frames and saves to disk.

        # Arguments
            file_path: path to video file.
            video_id: uuid of video.
    """
    video = cv2.VideoCapture(file_path)

    print("Processing video to frames...")

    while True:
        ret, frame = video.read()

        if not ret:
            break

        frame_id = f'{video_id}-{video.get(cv2.CAP_PROP_POS_MSEC)}'
        file_name = add_file_extension(frame_id, '.jpg')

        save_standard_image(frame, frame_id, file_name, 'np_array')
