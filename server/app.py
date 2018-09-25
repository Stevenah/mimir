from flask import Flask

from blueprints.pages import mod as pages_mod
from blueprints.cnn import mod as cnn_mod
from blueprints.files import mod as files_mod

from argparse import ArgumentParser

from models import Architecture, Image, Visualization, db

from model import ModelHelper

import os

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
        
def setup_app():

    app = Flask(__name__)

    app.config.from_pyfile('../config/app.conf')

    db.init_app(app)

    app.register_blueprint(pages_mod)
    app.register_blueprint(files_mod)
    app.register_blueprint(cnn_mod)

    if not os.path.isfile('/srv/mimir/mimir.db'):
        print("database initialization...")
        setup_database(app)

    return app

def setup_database(app):
    with app.app_context():
        db.create_all()

if __name__ == '__main__':

    app = setup_app()

    args = server_arg_parser()

    port  = args.port
    host  = args.host
    debug = args.debug

    print(f"Starting app on host {host} port {port}...")
    
    app.run(host=host, debug=debug)
