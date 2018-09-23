from flask import Flask

from blueprints.pages import mod as pages_mod
from blueprints.cnn import mod as cnn_mod
from blueprints.files import mod as files_mod

from argparse import ArgumentParser

from models import Architecture, Image, Visualization, db

from model import ModelHelper
from utils.file_utils import initialize_directories

import os
import shutil
import urllib

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def server_arg_parser():
    """ Gets argument parser for server.
        # Returns
            argument parser.
    """
    ap = ArgumentParser()

    ap.add_argument('-p', '--port', help='set the port used by the server', type=int, default=5000)
    ap.add_argument('--host', help='set the host used by the server', default='0.0.0.0')
    ap.add_argument('-d', '--debug', help='set the debug option', default=False)

    return ap.parse_args()


def setup_default_data():

    for model_pair in default_data:

        if not os.path.exists(model_pair[2]):
            print(f"Downloading {model_pair[0]}...")
            download_file(model_pair[4], model_pair[2])
            download_file('https://www.dropbox.com/s/pki880covt6bki1/kvasir.json?dl=1', model_pair[3])

        model = Architecture()
        
        model.model_name = model_pair[0]
        model.dataset_name = model_pair[1]
        model.model_file = open(model_pair[2], 'rb').read()
        model.class_file = open(model_pair[3], 'rb').read()

        if model_pair[0] == 'VGG-16':
            shutil.copy2(model_pair[2], '/tmp/model.h5')
            shutil.copy2(model_pair[3], '/tmp/class.json')
            model.active = True
            
        db.session.add(model)
        db.session.commit()
        
def setup_app():

    app = Flask(__name__)

    app.config.from_pyfile('../config/app.conf')

    db.init_app(app)

    app.register_blueprint(pages_mod)
    app.register_blueprint(files_mod)
    app.register_blueprint(cnn_mod)

    if not os.path.isfile('./mimir.db'):
        print("database initialization...")
        setup_database(app)

    if not os.path.isfile('./tmp/model.h5'):
        shutil.copy2(default_data[1][2], '/tmp/model.h5')
        shutil.copy2(default_data[1][3], '/tmp/class.json')

    app.config['MODEL'] = ModelHelper()

    return app

def setup_database(app):

    with app.app_context():
        db.create_all()
        initialize_directories()
        setup_default_data()

def download_file(url, dest):
    urllib.request.urlretrieve(url, dest)

if __name__ == '__main__':

    app = setup_app()

    args = server_arg_parser()

    port  = args.port
    host  = args.host
    debug = args.debug

    print(f"Starting app on host {host} port {port}...")
    
    app.run(host=host, debug=debug)
