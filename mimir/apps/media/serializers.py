from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from .models import Image

class ImageSerializer(serializers.ModelSerializer):
    
    image=serializers.ImageField()
    
    class Meta:
         model=Image
         fields= [ 'image' ]

    def create(self, validated_data):
        image=validated_data.pop('image')
        return Image.objects.create(image=image)
