from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from ..models import Image
from .. import serializers

class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ImageSerializer
    queryset = Image.objects.all()

    @action(methods=['get'], detail=True)
    def gradcam(self, request, pk=None):
        pass
    
    @action(methods=['get'], detail=True)
    def saliency(self, request, pk=None):
        pass

    @action(methods=['get'], detail=True)
    def guided(self, request, pk=None):
        pass