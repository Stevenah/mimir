from flask import Flask

from blueprints.pages import mod as pages_mod
from blueprints.cnn import mod as cnn_mod
from blueprints.files import mod as files_mod

from models.Architecture import Architecture
from models.Image import Image
from models.Visualization import Visualization

from database import db
from model import ModelHelper
from utils.kvasir_utils import kvasir_index_label
from utils.util import server_arg_parser

import os
import shutil

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

default_data=[
    ("Inception-V3-NON", "Non-processed Kvasir (v2)", "../model/inceptionv3.h5"),
    ("VGG-16-NON", "Non-processed Kvasir (v2)", "../model/vgg16.h5"),
    ("VGG-19-NON", "Non-processed Kvasir (v2)", "../model/vgg19.h5"),
    ("ResNet-50-NON", "Non-processed Kvasir (v2)", "../model/resnet50.h5"),
    ("Xeception-NON", "Non-processed Kvasir (v2)", "../model/xception.h5"),
]


def setup_app():
    app = Flask(__name__)

    app.config.from_pyfile('../config/app.conf')

    app.config['MODEL_CLASS_LABELS'] = kvasir_index_label
    class_labels = app.config['MODEL_CLASS_LABELS']
    app.config['MODEL'] = ModelHelper(classes=class_labels)

    db.init_app(app)

    app.register_blueprint(pages_mod)
    app.register_blueprint(files_mod)
    app.register_blueprint(cnn_mod)

    return app

def setup_database(app):
    with app.app_context():
        db.create_all()   

        for model_pair in default_data:
            model = Architecture()
            
            model.model_name = model_pair[0]
            model.dataset_name = model_pair[1]
            model.model_file = open(model_pair[2], 'rb').read()

            if model_pair[0] == 'VGG-16-NON':
                shutil.copy2(model_pair[2], '/tmp/model.h5')
                model.active = True

            db.session.add(model)
            db.session.commit()

if __name__ == '__main__':

    app = setup_app()

    if not os.path.isfile('./mimir.db'):
        print("database initialization...")
        setup_database(app)

    args = server_arg_parser()

    port  = args.port
    host  = args.host
    debug = args.debug

    print(f"Starting app on host {host} port {port}...")
    
    # app = create_app()
    app.run(host=host, debug=debug)
