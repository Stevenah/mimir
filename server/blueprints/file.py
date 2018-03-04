from flask import Blueprint, current_app as app
from flask.json import jsonify

from blueprints.utils import *

import flask
import os

mod = Blueprint('file', __name__, url_prefix='/api/file')

@mod.route('/upload', methods=['POST'])
def upload():
    
    response = {
        'status': 400,
        'success': False
    }

    _ = handle_upload(flask.request.files['qqfile'], flask.request.form)    
    response['success'] = True
    response['status'] = 200

    return jsonify(response)

@mod.route('/get/all', methods=['GET'])
def all():    
    response = {
        'status': 400,
        'success': False
    }

    image_filter = flask.request.args.get('filterType', 'original')

    if flask.request.method == 'GET':

        files = []

        for (file_str, filename), image_id in read_all_image(image_filter):
            files.append({
                'uuid': image_id,
                'name': filename,
                'filter': image_filter,
                'type': 'image',
                'file': base64.b64encode(file_str).decode('UTF-8')
            })

        response['files'] = files
        response['success'] = True
        response['status'] = 200

    return jsonify(response)


@mod.route('/visualize/<image_id>', methods=['GET', 'DELETE'])
def visualize(image_id):
    
    response = {
        'status': 400,
        'success': False
    }

    model = app.config['MODEL']

    layer_id = flask.request.args.get('layerId', '0')
    class_id = flask.request.args.get('classId', '0')

    if flask.request.method == 'GET':
    
        visualizations = {
            'gradcam': 'gradCam',
            'guided_gradcam': 'guidedGradCam'
        }

        image = np_read_image(image_id, 'original')
        model.visualize_image(image, image_id, layer_id, int(class_id))

        for visualization in visualizations:
            vis_id = model.get_image_id(image_id, visualization, layer_id, class_id)
            file_str, filename = read_image(vis_id, visualization)
            response[visualizations[visualization]] = {
                'name': filename,
                'source': base64.b64encode(file_str).decode('UTF-8'),
                'filter': visualization
            }

        response['success'] = True
        response['status'] = 200

    return jsonify(response)


@mod.route('/image/<image_id>', methods=['GET', 'POST', 'DELETE'])
def get(image_id):
    
    response = {
        'status': 400,
        'success': False
    }

    if flask.request.method == 'GET':            

        file_str, filename = read_image(image_id, image_filter)
        
        response['file'] = {}

        # response['file']['uuid'] = image_id
        response['file']['name'] = filename
        response['file']['filter'] = image_filter
        response['file']['file'] = base64.b64encode(file_str).decode('UTF-8')

        response['success'] = True
        response['status'] = 200

    if flask.request.method == 'DELETE':
        handle_delete(image_id)
        response['success'] = True
        response['status'] = 200

    return jsonify(response)

