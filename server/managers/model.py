from models.flask_models import NeuralNet
from helpers.keras import ModelHelper

class ModelManager():

    def __init__(self):
        pass
        # active_model_id = NeuralNet.get_active().id
        # self.activate(active_model_id)

    def get(self):
        return self.active
    
    def delete(self):
        pass

    def activate(self, modsel_id):
        NeuralNet.activate(model_id)
        self.active = ModelHelper(active_model)

model_manager = ModelManager()