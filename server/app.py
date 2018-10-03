from flask import Flask
from argparse import ArgumentParser

from blueprints.pages import mod as pages_mod
from blueprints.vision import mod as vision_mod
from blueprints.media import mod as media_mod
from blueprints.nn import mod as nn_mod

from helpers.tensorflow import register_guided_relu
from models.flask_models import db

import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def server_arg_parser():
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
    app.register_blueprint(media_mod)
    app.register_blueprint(vision_mod)
    app.register_blueprint(nn_mod)

    mimir_storage = app.config[ 'MIMIR_STORAGE' ]

    if not os.path.isfile(f'{ mimir_storage }/mimir.db'):
        print('database initialization...')
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

    print(f'Starting app on host {host} port {port}...')
    
    app.run(host=host, debug=debug)
