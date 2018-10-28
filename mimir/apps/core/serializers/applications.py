from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from ..models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    
    class Meta:
         model = Application
         fields = [ 'name', 'description' ]