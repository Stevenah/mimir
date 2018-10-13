
from models.flask_models import CHUNK_STORAGE_PATH, VIDEO_STORAGE_PATH, Image

from scipy.misc import imread

import os
import shutil

def load(image_path, as_type='np_array'):

    if as_type == 'np_array':
        return imread(path)

    if as_type == 'base_64':
        with open(path, 'rb') as f:
            return base64.b64encode(f.read()).decode('UTF-8')

    if as_type == 'string':
        with open(path, 'rb') as f:
            return f.read()

    raise NotImplementedError(f'Support for { as_type } is currenlty not supported!')

def upload_image(f, form_attributes):
    chunked = False
    chunk_dir = None

    file_name = form_attributes['qqfilename']
    file_id = form_attributes['qquuid']


    if 'qqtotalparts' in form_attributes:
        chunked = True
        chunk_size = int(form_attributes['qqtotalparts'])
        chunk_index = int(form_attributes['qqpartindex'])
        chunk_dir = os.path.join(CHUNK_STORAGE_PATH, file_id)
        if not os.path.exists(chunk_dir):
            os.makedirs(chunk_dir)

    if chunked and chunk_size > 1:
        with open(os.path.join(chunk_dir, chunk_index), 'wb+') as chunk:
            chunk.write(f.read())
        
    if chunked and (chunk_size - 1 == chunk_index):
        
        file_path = os.path.join(VIDEO_STORAGE_PATH, file_id)

        with open(file_path, 'wb+') as f:
            for chunk_index in range(chunk_size):
                chunk = os.path.join(chunk_dir, str(chunk_index))
                with open(chunk, 'rb') as source:
                    f.write(source.read())

        shutil.rmtree(chunk_dir)
    
    if not chunked:
        Image.create(f, file_name)