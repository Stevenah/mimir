from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from keras.models import load_model

from ..models import NeuralNet

class NeuralNetSerializer(serializers.ModelSerializer):

    class Meta:
         model=NeuralNet
         fields=[ 'name', 'pk' ]
        

class NeuralNetModelSerializer(serializers.ModelSerializer):

    class Meta:
         model=NeuralNet
         fields=[ 'model_file' ]