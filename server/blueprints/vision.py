from flask import Blueprint
from flask.json import jsonify

from models.flask_models import Image
from managers.model import model_manager

import flask

mod = Blueprint('vision', __name__, url_prefix='/api/vision')

@mod.route('/predict/<image_id>', methods=[ 'GET' ])
def predict(image_id):

    response = {
        'status': 400,
        'success': False,
        'payload': { }
    }
    
    if flask.request.method == 'GET':
        model = model_manager.get()
        
        response['classification'] = model.predict(Image.get(image_id))
        response['success'] = True
        response['status'] = 200

    return jsonify(response)

@mod.route('/visualize/<image_id>', methods=[ 'GET' ])
def visualize(image_id):

    response = {
        'status': 400,
        'success': False,
        'payload': { }
    }

    if flask.request.method == 'GET':

        model = model_manager.get_active()

        layer_id = flask.request.args.get('layerId', '0')
        class_id = flask.request.args.get('classId', '0')

        image = Image.get(image_id)

        model.cam(image, image_id, layer_id, class_id)
        model.guided_cam(image, image_id, layer_id, class_id)

        response['cam'] = image.load_cam(layer_id, class_id, as_type='base64')
        response['guidedCam'] = image.load_guided_cam(layer_id, class_id, as_type='base64')
        response['success'] = True
        response['status'] = 200

    return jsonify(response)