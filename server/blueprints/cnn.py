from flask import Blueprint, current_app as app
from flask.json import jsonify

from utils.file_utils import *

import flask
import os

mod = Blueprint('cnn', __name__, url_prefix='/api/cnn')

@mod.route('/layers', methods=['GET'])
def layers():
    """ Gets layers of underlying cnn
    
        # Returns
            jsonified list of layers.
    """
    response = {
        'status': 400,
        'payload': {}
    }
    
    if flask.request.method == 'GET':
        model = app.config['MODEL']
        response['layers'] = model.get_layers()
        response['status'] = 200

    return jsonify(response)

@mod.route('/classes', methods=['GET'])
def classes():
    """ Gets classes of underlying cnn
    
        # Returns
            jsonified list of classes.
    """
    response = {
        'status': 400,
        'payload': {}
    }
    
    if flask.request.method == 'GET':
        model = app.config['MODEL']
        response['classes'] = model.get_classes()
        response['status'] = 200

    return jsonify(response)

@mod.route('/classify/<image_id>', methods=['GET'])
def classify(image_id):
    """ Classifies image based on given image id.

        # Arguments
            image_id: id of image to be classified.
    
        # Returns
            Labels and prediction of classified image.
    """
    response = {
        'status': 400,
        'payload': {}
    }
    
    if flask.request.method == 'GET':
        model = app.config['MODEL']
        image = load_standard_image(image_id, as_type='np_array')
        image = model.prepare_image(image)
        response['classification'] = model.labeled_predictions(image)
        response['status'] = 200

    return jsonify(response)

@mod.route('/visualize/<image_id>', methods=['GET', 'DELETE'])
def visualize(image_id):
    """ visualizes image based on given image id.

        # Arguments
            image_id: id of image to be visualized.
    
        # Returns
            grad-CAM and guided grad-CAM representation of given image.
    """
    response = {
        'status': 400,
        'success': False
    }

    if flask.request.method == 'GET':

        model = app.config['MODEL']

        layer_id = flask.request.args.get('layerId', '0')
        class_id = flask.request.args.get('classId', '0')

        image = load_standard_image(image_id, as_type='np_array')

        model.visualize_image(image, image_id, layer_id, class_id)

        response['gradCam'] = load_gradcam_image(image_id, layer_id, class_id, as_type='base_64')
        response['guidedGradCam'] = load_guided_gradcam_image(image_id, layer_id, class_id, as_type='base_64')

        response['success'] = True
        response['status'] = 200

    return jsonify(response)