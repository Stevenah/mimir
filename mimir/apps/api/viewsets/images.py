from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.parsers import FormParser, MultiPartParser

from ..models import Image
from .. import serializers

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = serializers.ImageSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(
            imagefile=self.request.data.get('imagefile'))