from rest_framework.test import APIRequestFactory
from django.test import TestCase, Client
                                           
from django.core.files.images import ImageFile
from .models import Image, NeuralNet

import base64
import json
import os

TEST_RESOURCE_PATH = '/Users/stevenah/github/mimir/'

TEST_IMAGE = os.path.join(TEST_RESOURCE_PATH, 'hello.png')
TEST_NETWORK_FILE = os.path.join(TEST_RESOURCE_PATH, 'model.h5')

class ImageTest(TestCase):

    def setUp(self):

        self.client = Client()
        self.response = None
        
        with open(TEST_IMAGE, 'rb') as image_file:
            Image.objects.create(image=ImageFile(image_file))

    def test_post_image(self):
        with open(TEST_IMAGE, 'rb') as image_file:
            self.response = self.client.post('/api/images/', { 'image': image_file })

    def test_get_images(self):
        self.response = self.client.get('/api/images/')
        self.assertEqual(len(self.response.data), 1)

    def test_get_image(self):
        self.response = self.client.get('/api/images/1')


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

class DatasetTest(TestCase):

    def setUp(self):

        self.client = Client()
        self.response = None
        
    def test_get_neural_nets(self):
        self.response = self.client.get('/api/datasets/')
        self.assertEqual(len(self.response.data), 0)