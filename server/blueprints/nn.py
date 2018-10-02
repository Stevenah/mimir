from flask import Blueprint, current_app as app
from flask.json import jsonify

from models import NeuralNet, NeuralNet, db
from models import MODEL_STORAGE_PATH

from managers import model_manager

import flask
import os

mod = Blueprint('nn', __name__, url_prefix='/api/nn')

def model_upload(form_attributes):

        submission_id = form_attributes['submission_id']
        button_id = form_attributes['buttonId']
        file_name = form_attributes['qqfilename']

        model = NeuralNet.create(submission_id)

        with open(os.path.join(MODEL_STORAGE_PATH, file_name), 'wb+') as f:
            f.write(file.read())

        if model is None:

            model_file = open(file_path, 'rb').read() if button_id == 'model_file_input' else None
            class_file = open(file_path, 'rb').read() if button_id == 'class_file_input' else None

            model = Architecture(model_name, dataset_name, description,
                model_file, class_file, submission_id)

            db.session.add(model)
            db.session.commit()
            
        else:
            if button_id == 'model_file_input':
                model.model_file = open(file_path, 'rb').read()
            else:
                model.class_file = open(file_path, 'rb').read()
            db.session.commit()

@mod.route('/model', methods=['POST', 'GET'])
def model():

    response = {
        'status': 400,
        'success': False,
        'payload': {}
    }

    if flask.request.method == 'GET':
        response['models'] = NeuralNet.get_all()
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
        'payload': {}
    }

    if flask.request.method == 'DELETE':
        NeuralNet.remove(model_id)
        response['success'] = True
        response['status'] = 200

    return jsonify(response)

@mod.route('/model/<model_id>/activate', methods=['POST'])
def activate():

    response = {
        'status': 400,
        'success': False,
        'payload': {}
    }

    if flask.request.method == 'POST':
        NeuralNet.activate(model_id)
        response['success'] = True
        response['status'] = 200

    return jsonify(response)

@mod.route('/models', methods=['GET'])
def models():

    response = {
        'status': 400,
        'success': False,
        'payload': {}
    }

    if flask.request.method == 'GET':
        response['models'] = NeuralNet.get_all()
        response['success'] = True
        response['status'] = 200

    return jsonify(response)


@mod.route('/model/<model_id>/meta', methods=['GET'])
def model_info():

    response = {
        'status': 400,
        'success': False,
        'payload': {}
    }

    if flask.request.method == 'GET':
        model_manager.get_metadata(model_id)
        response['status'] = 200
        response['success'] = True

    return jsonify(response)
