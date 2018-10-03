from flask import Blueprint
from flask.json import jsonify

from managers.model import model_manager

import flask

mod = Blueprint('nn', __name__, url_prefix='/api/nn')

@mod.route('/model', methods=['POST', 'GET'])
def model():

    response = {
        'status': 400,
        'success': False,
        'payload': { }
    }

    if flask.request.method == 'GET':
        response['models'] = model_manager.get()
        response['success'] = True
        response['status'] = 200

    if flask.request.method == 'POST':
        model_upload(flask.request.form)
        response['success'] = True
        response['status'] = 200

    return jsonify(response)

@mod.route('/model/<model_id>', methods=['DELETE'])
def specific_model():

    response = {
        'status': 400,
        'success': False,
        'payload': { }
    }

    if flask.request.method == 'DELETE':
        model_manager.delete(model_id)
        response['success'] = True
        response['status'] = 200

    return jsonify(response)

@mod.route('/model/activate/<model_id>', methods=['POST'])
def activate():

    response = {
        'status': 400,
        'success': False,
        'payload': { }
    }

    if flask.request.method == 'POST':
        model_manager.activate(model_id)
        response['success'] = True
        response['status'] = 200

    return jsonify(response)

@mod.route('/model/<model_id>/meta', methods=['GET'])
def model_info():

    response = {
        'status': 400,
        'success': False,
        'payload': { }
    }

    if flask.request.method == 'GET':
        model_manager.get_metadata(model_id)
        response['status'] = 200
        response['success'] = True

    return jsonify(response)
