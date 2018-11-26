from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from keras.models import load_model

from ..models import NeuralNet, Dataset

class DatasetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Dataset
        fields = ('id', 'dataset_categories')
        depth = 2

class NeuralNetSerializer(serializers.ModelSerializer):

    dataset = DatasetSerializer()

    class Meta:
        model=NeuralNet
        fields=[ 'name', 'pk', 'dataset' ]
        depth = 1
        

        

class NeuralNetModelSerializer(serializers.ModelSerializer):

    class Meta:
         model=NeuralNet
         fields=[ 'model_file' ]