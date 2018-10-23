from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from ..models import NeuralNet

class NeuralNetSerializer(serializers.ModelSerializer):

    class Meta:
         model=NeuralNet
         fields=[ 'name' ]
        