from flask import Blueprint, current_app as app
from flask.json import jsonify

from models import Architecture, KerasModel, db
from models import MODEL_STORAGE_PATH

from managers import model_manager

import flask
import os

mod = Blueprint('nn', __name__, url_prefix='/api/nn')

def upload(form_attributes):

        submission_id = form_attributes['submission_id']
        button_id = form_attributes['buttonId']
        file_name = form_attributes['qqfilename']

        model = KerasModel.get(submission_id)

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
        'payload': {}
    }

    if flask.request.method == 'GET':
        response['models'] = model_manager.active()
        response['success'] = True
        response['status'] = 200

    if flask.request.method == 'POST':
        upload(flask.request.form)
        response['success'] = True
        response['status'] = 200

    return jsonify(response)

@mod.route('/model/<model_id>', methods=['GET', 'DELETE', 'POST'])
def specific_model():

    response = {
        'status': 400,
        'payload': {}
    }

    if flask.request.method == 'DELETE':
        KerasModel.remove(model_id)
        response['success'] = True
        response['status'] = 200

    if flask.request.method == 'POST':
        model_manager.activate(model_id)
        response['success'] = True
        response['status'] = 200

@mod.route('/models', methods=['POST', 'GET'])
def models():

    response = {
        'status': 400,
        'payload': {}
    }

    if flask.request.method == 'GET':
        response['models'] = model_manager.get_all()
        response['success'] = True
        response['status'] = 200

    return jsonify(response)


@mod.route('/model/<model_id>/meta', methods=['GET'])
def model_info():

    response = {
        'status': 400,
        'payload': {}
    }

    if flask.request.method == 'GET':
        model_manager.get_metadata(model_id)
        response['status'] = 200
        response['success'] = True

    return jsonify(response)
