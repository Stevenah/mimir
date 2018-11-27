from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from keras.models import load_model

from ..models import NeuralNetwork, Dataset, DatasetCategory, Category

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model=Category
        fields=[ 'name' ]

class DatasetCategoriesSerializer(serializers.ModelSerializer):
    
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
     )

    class Meta:
        model=DatasetCategory
        fields=[ 'category' ]
        depth=1

class DatasetSerializer(serializers.ModelSerializer):

    dataset_categories = DatasetCategoriesSerializer
    
    class Meta:
        model=Dataset
        fields = ('id', 'dataset_categories')
        depth = 2

class NeuralNetworkSerializer(serializers.ModelSerializer):

    dataset = DatasetSerializer()

    class Meta:
        model=NeuralNetwork
        fields=[ 'name', 'pk', 'dataset' ]
        depth = 1

class NeuralNetworkModelSerializer(serializers.ModelSerializer):

    class Meta:
         model=NeuralNetwork
         fields=[ 'model_file' ]