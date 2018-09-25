from flask import Blueprint, current_app as app
from flask.json import jsonify

from models import Architecture, Image, db
from manager import model_manager

from utils.file_utils import *

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
        image = Image.get(image_id, as_type='np_array')
        response['classification'] = model.predict(image, with_labels=True)
        response['status'] = 200

    return jsonify(response)

@mod.route('/reclassify', methods=['POST'])
def reclassify():

    response = {
        'status': 400,
        'payload': {}
    }
    
    if flask.request.method == 'POST':
        model = model_manager.get_active()
        for image in Image.query.all():
            prediction, label, class_index = model.predict(image.path, with_labels=True)
            Image.update(image.id, label=label,
                prediction=prediction, class_id=int(class_index))
        response['status'] = 200
        response['success'] = True

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

        image = Image.get(image_id, as_type='np_array')

        model.visualize_image(image, image_id, layer_id, class_id)

        response['gradCam'] = load_visualization(image_id, layer_id, class_id, 'gradcam', as_type='base_64')
        response['guidedGradCam'] = load_visualization(image_id, layer_id, class_id, 'guided_gradcam', as_type='base_64')

        response['success'] = True
        response['status'] = 200

    return jsonify(response)