from flask import Blueprint, request
from flask.json import jsonify

from models import Image
from models import CHUNK_STORAGE_PATH, VIDEO_STORAGE_PATH

import os
import shutil

mod = Blueprint('media', __name__, url_prefix='/api/media')

def image_upload(f, form_attributes):
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


@mod.route('/image', methods=['GET', 'POST'])
def route_images():
    
    response = {
        'status': 400,
        'success': False
    }

    if request.method == 'GET':
        response['images'] = Image.load_all(as_type='base_64')
        response['success'] = True
        response['status'] = 200

    if request.method == 'POST':
        image_upload(request.files['qqfile'], request.form)
        response['success'] = True
        response['status'] = 200

    return jsonify(response)

@mod.route('/image/<image_id>', methods=['GET', 'DELETE', 'PUT'])
def route_image(image_id):
    
    response = {
        'status': 400,
        'success': False
    }
    
    if request.method == 'GET':
        response['image'] = Image.load(image_id, as_type='base_64')
        response['success'] = True
        response['status'] = 200

    if request.method == 'DELETE':
        Image.remove(image_id)
        response['success'] = True
        response['status'] = 200

    return jsonify(response)