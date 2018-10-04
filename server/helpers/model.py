from models.flask_models import NeuralNet, Dataset

def upload_model(keras_model_file, form_attributes):

        model_name=form_attributes['model_name']
        dataset_id=form_attributes['dataset_id']
        description=form_attributes['description']

        NeuralNet.create(keras_model_file, 
                model_name, dataset_id, description)

def upload_dataset(class_file, form_attributes):

        dataset_name=form_attributes['dataset_name']
        description=form_attributes['description']

        Dataset.create(class_file, dataset_name, description)
