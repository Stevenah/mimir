from flask import Blueprint, request, current_app as app
from flask.json import jsonify

from utils.file_utils import *

mod = Blueprint('upload', __name__, url_prefix='/api/files')

@mod.route('/upload', methods=['POST'])
def route_upload():
    """ Upload files route

        # Returns
            standard response.
    """
    response = {
        'status': 400,
        'success': False
    }

    if request.method == 'POST':
        upload(request.files['qqfile'], request.form)
        response['success'] = True
        response['status'] = 200

    return jsonify(response)

@mod.route('/images', methods=['GET'])
def route_images():
    """ Get all standard iamges from standard directory.

        # Returns
            returns jsonified list of images.
    """
    response = {
        'status': 400,
        'success': False
    }

    if request.method == 'GET':
        response['images'] = load_images()
        response['status'] = 200
        response['success'] = True

    return jsonify(response)


@mod.route('/images/<image_id>', methods=['POST', 'GET', 'DELETE'])
def route_image(image_id):
    """ Get  standard iamge from standard directory.

        # Arguments
            image_id: id of image to be retrieved.

        # Returns
            returns image with given image_id.
    """
    response = {
        'status': 400,
        'success': False
    }
    
    if request.method == 'GET':
        response['success'] = False
        response['status'] = 501

    if request.method == 'DELETE':
        response['success'] = False
        response['status'] = 501

    return jsonify(response)