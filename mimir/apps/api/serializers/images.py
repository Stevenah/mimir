from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from ..models import Image

class ImageSerializer(serializers.ModelSerializer):
    
    source = serializers.ImageField()
    
    class Meta:
         model=Image
         fields= [ 'source' ]

    def create(self, validated_data):
        image=validated_data.pop('source')
        return Image.objects.create(sourec=image)