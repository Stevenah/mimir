from flask import Flask

from blueprints.pages import mod as pages_mod
from blueprints.cnn import mod as cnn_mod
from blueprints.files import mod as files_mod

from models.Architecture import Architecture
from models.Image import Image
from models.Visualization import Visualization

from database import db
from model import ModelHelper
from utils.util import server_arg_parser
from utils.file_utils import initialize_directories

import os
import shutil
import urllib

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

default_data=[
    ("Inception-V3", "Non-processed Kvasir (v2)", "../model/inceptionv3.h5", "../model/kvasir.json", "https://www.dropbox.com/s/t0lxg8ei0g3etye/inceptionv3.h5?dl=1"),
    ("VGG-16", "Non-processed Kvasir (v2)", "../model/vgg16.h5", "../model/kvasir.json", "https://www.dropbox.com/s/vonhjmv4qzorhex/vgg16.h5?dl=1"),
    ("VGG-19", "Non-processed Kvasir (v2)", "../model/vgg19.h5", "../model/kvasir.json", "https://www.dropbox.com/s/t3v0rktokali77m/vgg19.h5?dl=1"),
    ("ResNet-50", "Non-processed Kvasir (v2)", "../model/resnet50.h5", "../model/kvasir.json", "https://www.dropbox.com/s/0vzgs2e341k0j9u/resnet50.h5?dl=1"),
    ("Xeception", "Non-processed Kvasir (v2)", "../model/xception.h5", "../model/kvasir.json", "https://www.dropbox.com/s/h314gq7ly82wgml/xception.h5?dl=1"),
    
    ("Inception-V3", "blacked-out-processed Kvasir (v2)", "../model/proc_inceptionv3.h5", "../model/kvasir.json"),
    ("VGG-16", "blacked-out-processed Kvasir (v2)", "../model/proc_vgg16.h5", "../model/kvasir.json"),
    ("VGG-19", "blacked-out-processed Kvasir (v2)", "../model/proc_vgg19.h5", "../model/kvasir.json"),
    ("ResNet-50", "blacked-out-processed Kvasir (v2)", "../model/proc_resnet50.h5", "../model/kvasir.json"),
    ("Xeception", "blacked-out-processed Kvasir (v2)", "../model/proc_xception.h5", "../model/kvasir.json"),
    
    ("Inception-V3", "blacked-out-borders-removed-processed Kvasir (v2)", "../model/proc2_inceptionv3.h5", "../model/kvasir.json"),
    ("VGG-16", "blacked-out-borders-removed-processed Kvasir (v2)", "../model/proc2_vgg16.h5", "../model/kvasir.json"),
    ("VGG-19", "blacked-out-borders-removed-processed Kvasir (v2)", "../model/proc2_vgg19.h5", "../model/kvasir.json"),
    ("ResNet-50", "blacked-out-borders-removed-processed Kvasir (v2)", "../model/proc2_resnet50.h5", "../model/kvasir.json"),
    ("Xeception", "blacked-out-borders-removed-processed Kvasir (v2)", "../model/proc2_xception.h5", "../model/kvasir.json")
]

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
    """ Initialize application
    """
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
    """ Initialize database and setup required directories
    """
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
