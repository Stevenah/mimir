from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from ..models import NeuralNet
from .. import serializers

class NeuralNetViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.NeuralNetSerializer
    queryset = NeuralNet.objects.all()

    @action(methods=['post'], detail=True)
    def activate(self, request, pk=None):
        print("hello", pk)