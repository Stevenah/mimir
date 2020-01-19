
import os
import flask
import argparse

from blueprints import pages_mod
from blueprints import cnn_mod
from blueprints import images_mod

from models import NeuralNetwork
from models import Image
from models import Explanation

from database import db

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

default_data = {
    "Inception-V3": {
        "url": "",
        "active": True
    }
}

default_dir = "./"
uploads_dir = "%s/uploads" % default_dir

if not os.path.isdir(uploads_dir):
    os.makedirs(uploads_dir)

def server_arg_parser():
    """ Gets argument parser for server.
        # Returns
            argument parser.
    """
    ap = argparse.ArgumentParser()

    ap.add_argument('-p', '--port', help='set the port used by the server', type=int, default=5000)
    ap.add_argument('--host', help='set the host used by the server', default='0.0.0.0')
    ap.add_argument('-d', '--debug', help='set the debug option', default=False)

    return ap.parse_args()

def setup_default_data():
    
    for model_name, model_config in default_data.items():

        model = NeuralNetwork()
        
        model.model_name = model_name
        model.active = model_config["active"]
        model.url = model_config["url"]
            
        db.session.add(model)
        db.session.commit()
        
def setup_app():
    app = flask.Flask(__name__)

    app.config.from_pyfile('../config/app.conf')

    db.init_app(app)

    app.register_blueprint(pages_mod)
    app.register_blueprint(images_mod)
    app.register_blueprint(cnn_mod)

    if not os.path.isfile('./mimir.db'):
        print("database initialization...")
        setup_database(app)

    return app

def setup_database(app):
    with app.app_context():
        db.create_all()
        setup_default_data()

if __name__ == '__main__':

    app = setup_app()

    args = server_arg_parser()

    port  = args.port
    host  = args.host
    debug = args.debug

    print(f"Starting app on host {host} port {port}...")
    
    app.run(host=host, debug=debug)
