from rest_framework.test import APIRequestFactory
from django.test import TestCase, Client
from django.core.files import File
                                           
from ..models import NeuralNet

import base64
import json
import os

TEST_RESOURCE_PATH = '/Users/stevenah/github/mimir/run/media'
TEST_NETWORK_FILE = os.path.join(TEST_RESOURCE_PATH, 'model.h5')

class NeuralTest(TestCase):

    def setUp(self):

        self.client = Client()
        self.response = None
        
        with open(TEST_NETWORK_FILE, 'rb') as model_file:
            NeuralNet.objects.create(model_file=File(model_file))
        
    def test_get_neural_nets(self):
        self.response = self.client.get('/api/networks/')
        self.assertEqual(len(self.response.data), 1)

    def test_activate_neural_net(self):
        self.response = self.client.post('/api/networks/1/activate/')
        self.assertEqual(NeuralNet.objects.get(pk=1).active, True)

    def test_layers_neural_net(self):
        self.response = self.client.get('/api/networks/1/layers/')