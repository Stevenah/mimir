from rest_framework import viewsets, permissions
from ..models import Image
from .. import serializers

class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ImageSerializer
    queryset = Image.objects.all()