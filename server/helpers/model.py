
from models.flask_models import NeuralNet, db
from models.flask_models import MODEL_STORAGE_PATH

import os

def upload_model(keras_model_file, form_attributes):
        model = NeuralNet.create(keras_model_file)
