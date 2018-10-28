from rest_framework.test import APIRequestFactory
from django.test import TestCase, Client

import json
import os

class AppsTest(TestCase):

    def setUp(self):

        self.client = Client()
        self.response = None
    
    def test_list_apps(self):
        self.response = self.client.get('/core/apps/')
        