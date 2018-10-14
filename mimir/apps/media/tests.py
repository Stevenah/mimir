from rest_framework.test import APIRequestFactory
from django.test import TestCase, Client
                                           
from django.core.files.images import ImageFile
from .models import Image

import base64
import json

class ImageTest(TestCase):

    def setUp(self):
        with open('/Users/stevenah/github/mimir/static/16614450.jpeg', 'rb') as image_file:
            Image.objects.create(image=ImageFile(image_file))

    def test_post_image(self):
        client = Client()
        response = None
        with open('/Users/stevenah/Pictures/16614450.jpeg', 'rb') as image_file:
            response = client.post('/media/images/', { 'image': image_file })

    def test_get_images(self):
        client = Client()
        response = client.get('/media/images/')
        self.assertEqual(len(response.data), 1)