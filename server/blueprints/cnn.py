from flask import Blueprint, current_app as app
from flask.json import jsonify

from models.Architecture import Architecture
from database import db

from utils.file_utils import *

import flask
import os

mod = Blueprint('cnn', __name__, url_prefix='/api/cnn')

@mod.route('/upload', methods=['POST'])
def upload():

    response = {
        'status': 400,
        'payload': {}
    }
    
    if flask.request.method == 'POST':

        submission_id = flask.request.form['submission_id']
        button_id = flask.request.form['buttonId']
        file_name = flask.request.form['qqfilename']

        model = Architecture.query.filter_by(submission_id=submission_id).first()

        file_path = f'/tmp/{file_name}'

        with open(file_path, 'wb+') as f:
            f.write(flask.request.files['qqfile'].read())

        if model is None:
            model = Architecture(
                model_name=flask.request.form['model_name'],
                dataset_name=flask.request.form['dataset_name'],
                description=flask.request.form['description'],
                model_file=open(file_path, 'rb').read() if button_id == 'model_file_input' else None,
                class_file=open(file_path, 'rb').read() if button_id == 'class_file_input' else None,
                submission_id=flask.request.form['submission_id'])
            db.session.add(model)
            db.session.commit()
        else:
            if button_id == 'model_file_input':
                model.model_file = open(file_path, 'rb').read()
            else:
                model.class_file = open(file_path, 'rb').read()
            db.session.commit()

        response['success'] = True
        response['status'] = 200

    return jsonify(response)

@mod.route('/delete/<model_id>', methods=['DELETE'])
def delete(model_id):

    response = {
        'status': 400,
        'payload': {}
    }

    if flask.request.method == 'DELETE':
        model = Architecture.query.filter_by(id=model_id).first()
        db.session.delete(model)
        db.session.commit()
        response['status'] = 200
        response['message'] = 'success'

    return jsonify(response)

@mod.route('/models', methods=['GET'])
def models():

    response = {
        'status': 400,
        'payload': {}
    }
    
    if flask.request.method == 'GET':
        response['models'] = [
            { 
                'id': model.id,
                'model': model.model_name,
                'dataset': model.dataset_name 
            } 
            for model in Architecture.query.with_entities(Architecture.id, Architecture.model_name, Architecture.dataset_name).all()
        ]
        response['success'] = True
        response['status'] = 200

    return jsonify(response)

@mod.route('/active', methods=['GET'])
def active():

    response = {
        'status': 400,
        'payload': {}
    }
    
    if flask.request.method == 'GET':
        model = Architecture.query.filter_by(active=True).first()
        response['model'] = {
            'name': model.model_name,
            'id': model.id
        } 
        response['success'] = True
        response['status'] = 200

    return jsonify(response)

@mod.route('/activate/<model_id>', methods=['POST'])
def activate(model_id):

    response = {
        'status': 400,
        'payload': {}
    }
    
    if flask.request.method == 'POST':
        app.config['MODEL'].swap_model(model_id)
        active_model = Architecture.query.filter_by(active=True).first()
        model = Architecture.query.filter_by(id=model_id).first()
        response['model'] = {
            'name': model.model_name,
            'id': model.id
        }

        active_model.active = False
        model.active = True

        db.session.add(active_model)
        db.session.add(model)
        db.session.commit()

        response['success'] = True
        response['status'] = 200

    return jsonify(response)
    

@mod.route('/available', methods=['GET'])
def available():

    response = {
        'status': 400,
        'payload': {}
    }
    
    if flask.request.method == 'GET':
        response['status'] = 200

    return jsonify(response)

@mod.route('/swap/<model_id>', methods=['GET'])
def swap(model_id):

    response = {
        'status': 400,
        'payload': {}
    }
    
    if flask.request.method == 'GET':
        model = app.config['MODEL']
        model.swap(model_id)
        response['status'] = 200

    return jsonify(response)


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
        response['layers'] = { layer_id: layer_name for layer_id, layer_name in enumerate(model.get_layers()) }
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

@mod.route('/reclassify', methods=['POST'])
def reclassify():
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

        image = load_image(image_id, as_type='np_array')
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

        image = load_image(image_id, as_type='np_array')

        model.visualize_image(image, image_id, layer_id, class_id)

        response['gradCam'] = load_visualization(image_id, layer_id, class_id, 'gradcam', as_type='base_64')
        response['guidedGradCam'] = load_visualization(image_id, layer_id, class_id, 'guided_gradcam', as_type='base_64')

        response['success'] = True
        response['status'] = 200

    return jsonify(response)
