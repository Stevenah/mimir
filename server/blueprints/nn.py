from flask import Blueprint, current_app as app
from flask.json import jsonify

from models import Architecture, db

from utils.file_utils import *

import flask
import os

mod = Blueprint('nn', __name__, url_prefix='/api/nn')

@mod.route('/model', methods=['POST', 'GET'])
def models():

    response = {
        'status': 400,
        'payload': {}
    }

    if flask.request.method == 'POST':

        submission_id = flask.request.form['submission_id']
        button_id = flask.request.form['buttonId']
        file_name = flask.request.form['qqfilename']

        upload_model(submission_id, button_id, file_name)

        response['success'] = True
        response['status'] = 200

    if flask.request.method == 'GET':
        response['models'] = get_available_models()

        response['success'] = True
        response['status'] = 200

    return jsonify(response)

@mod.route('/model/<model_id>', methods=['GET', 'DELETE', 'POST'])
def model():

    response = {
        'status': 400,
        'payload': {}
    }

    if flask.request.method == 'GET':
        pass

    if flask.request.method == 'DELETE':
        model = Architecture.query.filter_by(id=model_id).first()
        
        db.session.delete(model)
        db.session.commit()

        response['status'] = 200
        response['message'] = 'success'

    if flask.request.method == 'POST':
        app.config['MODEL'].swap_model(model_id)

        active_model = Architecture.query.filter_by(active=True).first()
        model = Architecture.query.filter_by(id=model_id).first()

        response['model'] = { 'name': model.model_name, 'id': model.id }

        active_model.active = False
        model.active = True

        db.session.add(active_model)
        db.session.add(model)
        db.session.commit()

        response['success'] = True
        response['status'] = 200


@mod.route('/model/<model_id>/<info_id>', methods=['GET'])
def model_info():

    response = {
        'status': 400,
        'payload': {}
    }

    if flask.request.method == 'GET':
        model = Architecture.query.filter_by(model_id=model_id).first()

        if info_id == 'layers':
            response['layers'] = { layer_id: layer_name for layer_id, layer_name in enumerate(model.get_layers()) }
            response['status'] = 200
        
        if info_id == 'classes':
            response['classes'] = model.get_classes()
            response['status'] = 200

@mod.route('/active', methods=['GET'])
def active():

    response = {
        'status': 400,
        'payload': {}
    }
    
    if flask.request.method == 'GET':
        model = Architecture.query.filter_by(active=True).first()
        response['model'] = { 'name': model.model_name, 'id': model.id } 
        response['success'] = True
        response['status'] = 200

    return jsonify(response)

def get_available_models():
    return [{ 
                'id': model.id,
                'model': model.model_name,
                'dataset': model.dataset_name 
        } for model in Architecture.query.with_entities(Architecture.id, Architecture.model_name, Architecture.dataset_name).all()
    ]

def upload_model(sumbission_id, button_id, file_name,
    file, model_name, dataset_name, description):

        model = Architecture.query.filter_by(submission_id=submission_id).first()

        file_path = f'/tmp/{file_name}'

        with open(file_path, 'wb+') as f:
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