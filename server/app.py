from flask import Flask
from flask_cors import CORS

from blueprints.pages import mod as pages_mod
from blueprints.model import mod as model_mod
from blueprints.visualize import mod as visualize_mod
from blueprints.file import mod as file_mod

from utils.modelhelper import ModelHelper
from utils.kvasir import KVASIR_CLASSIFICATION_LABELS
from utils.util import server_arg_parser

import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

app = Flask(__name__)
CORS(app)

app.config.from_pyfile('../config/app.conf')
app.config['MODEL_CLASS_LABELS'] = KVASIR_CLASSIFICATION_LABELS
app.config['MODEL'] = ModelHelper(
    classes=app.config['MODEL_CLASS_LABELS'],
    model_json=app.config['MODEL_JSON_PATH'],
    model_weights=app.config['MODEL_WEIGHTS_PATH']
)

app.register_blueprint(pages_mod)
app.register_blueprint(visualize_mod)
app.register_blueprint(model_mod)
app.register_blueprint(file_mod)


if __name__ == '__main__':

    args = server_arg_parser()

    port  = args.port
    host  = args.host
    debug = args.debug

    print(f"Starting app on host {host} port {port}...")
    
    # app = create_app()
    app.run(host=host, debug=debug)
