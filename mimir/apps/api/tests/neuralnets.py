from rest_framework.test import APIRequestFactory
from django.test import TestCase, Client
                                           
from .models import NeuralNet

import base64
import json
import os

TEST_RESOURCE_PATH = '/Users/stevenah/github/mimir/'

TEST_IMAGE = os.path.join(TEST_RESOURCE_PATH, 'hello.png')
TEST_NETWORK_FILE = os.path.join(TEST_RESOURCE_PATH, 'model.h5')

class NeuralTest(TestCase):

    def setUp(self):

        self.client = Client()
        self.response = None

        NeuralNet.objects.create(name="hello")
        
    def test_get_neural_nets(self):
        self.response = self.client.get('/api/networks/')
        self.assertEqual(len(self.response.data), 1)

    def test_activate_neural_net(self):
        self.response = self.client.post('/api/networks/0/activate')
        print(self.response)