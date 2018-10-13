from rest_framework.test import APIRequestFactory
from django.test import TestCase

import base64

class ImageTest(TestCase):

    def test_tests(self):

        encoded_string = None

        with open('/Users/stevenah/Pictures/16614450.jpeg', 'rb') as image_file:
            encoded_string = base64.b64encode(image_file.read())

        # Using the standard RequestFactory API to create a form POST request
        factory = APIRequestFactory()
        request = factory.post('/media/', {'image': encoded_string}, content_type='application/json')
