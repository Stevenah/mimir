from flask import Blueprint, render_template
from flask.json import jsonify

import flask
import cv2
import os

mod = Blueprint('pages', __name__)

@mod.route('/', defaults={'path': ''})
@mod.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')