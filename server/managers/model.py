from models.flask_models import NeuralNet
from helpers.keras import ModelHelper

class ModelManager():

    def init(self):

        active_model = NeuralNet.get_active()
        
        if active_model == None:
            active_model = NeuralNet.query.first()

        if active_model == None:
            self.active = None
        else:
            self.activate(active_model.id)

    def get(self):
        return self.active
    
    def activate(self, model_id):
        NeuralNet.activate(model_id)
        active_model = NeuralNet.get_active()
        self.active = ModelHelper(active_model)
        
model_manager = ModelManager()