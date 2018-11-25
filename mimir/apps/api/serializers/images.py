from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from ..models import Image

class ImageSerializer(serializers.ModelSerializer):
    
    imagefile = serializers.ImageField()
    
    class Meta:
         model = Image
         fields = [ 'imagefile', 'id' ]

    def create(self, validated_data):
        image=validated_data.pop('imagefile')
        return Image.objects.create(imagefile=image)