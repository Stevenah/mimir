from flask import Blueprint, request
from flask.json import jsonify

from models import Image

mod = Blueprint('media', __name__, url_prefix='/api/media')

@mod.route('/image', methods=['GET', 'POST'])
def route_images():
    
    response = {
        'status': 400,
        'success': False
        'payload': { }
    }

    if request.method == 'GET':
        response['images'] = Image.load_all(as_type='base_64')
        response['success'] = True
        response['status'] = 200

    if request.method == 'POST':
        upload_image(request.files['qqfile'], request.form)
        response['success'] = True
        response['status'] = 200

    return jsonify(response)

@mod.route('/image/<image_id>', methods=['GET', 'DELETE', 'PUT'])
def route_image(image_id):
    
    response = {
        'status': 400,
        'success': False,
        'payload': { }
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