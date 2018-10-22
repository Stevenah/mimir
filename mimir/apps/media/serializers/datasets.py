from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from ..models import Dataset

class DatasetSerializer(serializers.ModelSerializer):
    
    class Meta:
         model=Dataset