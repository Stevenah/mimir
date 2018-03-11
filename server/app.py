from flask import Flask
from flask_cors import CORS

from blueprints.pages import mod as pages_mod
from blueprints.cnn import mod as cnn_mod
from blueprints.files import mod as files_mod

from model import ModelHelper
from utils.kvasir_utils import kvasir_index_label
from utils.util import server_arg_parser

import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

app = Flask(__name__)
CORS(app)

app.config.from_pyfile('../config/app.conf')
app.config['MODEL_CLASS_LABELS'] = kvasir_index_label
app.config['MODEL'] = ModelHelper(
    classes=app.config['MODEL_CLASS_LABELS'],
    model_json=app.config['MODEL_JSON_PATH'],
    model_weights=app.config['MODEL_WEIGHTS_PATH']
)

app.register_blueprint(pages_mod)
app.register_blueprint(files_mod)
app.register_blueprint(cnn_mod)

if __name__ == '__main__':

    args = server_arg_parser()

    port  = args.port
    host  = args.host
    debug = args.debug

    print(f"Starting app on host {host} port {port}...")
    
    # app = create_app()
    app.run(host=host, debug=debug)
