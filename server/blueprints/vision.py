from flask import Blueprint, current_app as app
from flask.json import jsonify

from models import Architecture, Image, db
from manager import model_manager

import flask
import os

mod = Blueprint('nn', __name__, url_prefix='/api/vision')

@mod.route('/predict/<image_id>', methods=['GET'])
def classify(image_id):

    response = {
        'status': 400,
        'payload': {}
    }
    
    if flask.request.method == 'GET':
        model = model_manager.get_active()
        image = Image.load(image_id, as_type='np_array')
        
        response['classification'] = model.predict(image, with_labels=True)
        response['status'] = 200

    return jsonify(response)

@mod.route('/visualize/<image_id>', methods=['GET', 'DELETE'])
def visualize(image_id):

    response = {
        'status': 400,
        'success': False
    }

    if flask.request.method == 'GET':

        model = model_manager.get_active()

        layer_id = flask.request.args.get('layerId', '0')
        class_id = flask.request.args.get('classId', '0')

        image = Image.load(image_id, as_type='np_array')

        cam = model.cam(image, image_id, layer_id, class_id)
        guided_cam = model.guided_cam(image, image_id, layer_id, class_id)

        response['gradCam'] = load_visualization(image_id, layer_id, class_id, 'gradcam', as_type='base_64')
        response['guidedGradCam'] = load_visualization(image_id, layer_id, class_id, 'guided_gradcam', as_type='base_64')

        response['success'] = True
        response['status'] = 200

    return jsonify(response)