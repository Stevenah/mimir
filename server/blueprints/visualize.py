from flask import Blueprint, current_app as app
from flask.json import jsonify

from blueprints.utils import *
import flask
import cv2
import os

mod = Blueprint('analysis', __name__, url_prefix='/api/analyze')

def make_response(content, status):
    return {
        **content,
        'staus': status,
    }

@mod.route('/image/<image_id>', methods=['POST'])
def image(image_id):

    response = {
        'status': 400,
        'success': False,
    }

    if flask.request.method == 'POST':
        model = app.config['MODEL']

        threshold = flask.request.args.get('threshold', default=.1, type=int)
        layers = flask.request.args.get('layers', default=0, type=int)

        image = np_read_image(image_id, 'original')
        model.visualize_model(image, image_id)
        
        response['status'] = 200
        response['success'] = True

    return jsonify(response)