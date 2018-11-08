from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from ..models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    
    banner = Base64ImageField()

    class Meta:
         model = Application
         fields = [ 'name', 'description', 'banner', 'link' ]