from rest_framework.test import APIRequestFactory
from django.test import TestCase, Client
                                           
from .models import Dataset

import base64
import json
import os

class DatasetTest(TestCase):

    def setUp(self):

        self.client = Client()
        self.response = None
        
    def test_get_neural_nets(self):
        self.response = self.client.get('/api/datasets/')
        self.assertEqual(len(self.response.data), 0)