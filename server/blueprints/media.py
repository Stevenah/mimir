from flask import Blueprint, request, current_app as app
from flask.json import jsonify

from utils.file_utils import *

mod = Blueprint('media', __name__, url_prefix='/api/media')

@mod.route('/image', methods=['GET', 'POST'])
def route_images():
    
    response = {
        'status': 400,
        'success': False
    }

    if request.method == 'GET':
        response['images'] = load_images(True)
        response['status'] = 200
        response['success'] = True

    if request.method == 'POST':
        upload(request.files['qqfile'], request.form)
        response['success'] = True
        response['status'] = 200

    return jsonify(response)


@mod.route('/image/<image_id>', methods=['GET', 'DELETE'])
def route_image(image_id):
    
    response = {
        'status': 400,
        'success': False
    }
    
    if request.method == 'GET':
        response['image'] = load_image(image_id, 'base_64')
        response['success'] = True
        response['status'] = 200

    if request.method == 'DELETE':
        response['success'] = False
        response['status'] = 501

    return jsonify(response)