from flask import Blueprint, current_app as app
from flask.json import jsonify

from models import Architecture, db

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

        model = app.config['MODEL']

        image = load_image(image_id, as_type='np_array')
        image = model.prepare_image(image)

        response['classification'] = model.labeled_predictions(image)
        response['status'] = 200

    return jsonify(response)

@mod.route('/reclassify', methods=['POST'])
def reclassify():

    response = {
        'status': 400,
        'payload': {}
    }
    
    if flask.request.method == 'POST':

        model = app.config['MODEL']
        images = Image.query.all()

        for image in images:

            prediction, label, class_index = model.predict_from_path(image.path)

            image.label = label
            image.prediction = prediction
            image.class_index = int(class_index)

            db.session.add(image)
            db.session.commit()

        response['status'] = 200

    return jsonify(response)


@mod.route('/visualize/<image_id>', methods=['GET', 'DELETE'])
def visualize(image_id):

    response = {
        'status': 400,
        'success': False
    }

    if flask.request.method == 'GET':

        model = app.config['MODEL']

        layer_id = flask.request.args.get('layerId', '0')
        class_id = flask.request.args.get('classId', '0')

        image = load_image(image_id, as_type='np_array')

        model.visualize_image(image, image_id, layer_id, class_id)

        response['gradCam'] = load_visualization(image_id, layer_id, class_id, 'gradcam', as_type='base_64')
        response['guidedGradCam'] = load_visualization(image_id, layer_id, class_id, 'guided_gradcam', as_type='base_64')

        response['success'] = True
        response['status'] = 200

    return jsonify(response)