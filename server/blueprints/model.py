from flask import Blueprint, current_app as app
from flask.json import jsonify

from blueprints.utils import *

import flask
import cv2
import os

mod = Blueprint('model', __name__, url_prefix='/api/model')

@mod.route('/layers', methods=['GET'])
def layers():

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

    response = {
        'status': 400,
        'payload': {}
    }
    
    if flask.request.method == 'GET':
        model = app.config['MODEL']

        image = np_read_image(image_id)
        image = model.prepare_image(image)
        response['classes'] = model.labeled_predictions(image)
        response['status'] = 200

    return jsonify(response)
