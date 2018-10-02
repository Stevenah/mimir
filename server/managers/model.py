from model import NeuralNet
from helpers.keras import ModelHelper

class ModelManager():

    def __init__(self):
        active_model_id = NeuralNet.get_active_id()
        self.activate(active_model_id)

    def get(self):
        return self.active

    def activate(self, modsel_id):
        NeuralNet.activate(model_id)
        self.active = ModelHelper(active_model)

model_manager = ModelManager()