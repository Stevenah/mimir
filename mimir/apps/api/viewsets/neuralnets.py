from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status

from django_filters.rest_framework import DjangoFilterBackend

from keras.models import load_model

from ..serializers import NeuralNetworkSerializer
from ..models import NeuralNetwork
from .. import serializers

class NeuralNetViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.NeuralNetworkSerializer
    queryset = NeuralNetwork.objects.all()
    renderer_classes = (JSONRenderer, )
    filter_backends = (DjangoFilterBackend, )
    
    @action(methods=['get'], detail=True)
    def classes(self, request, pk=None):
        classes = NeuralNetwork.objects.get(pk=pk).dataset.dataset_categories.select_related().all().values('category__name', 'index')
        return Response(classes, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=True)
    def layers(self, request, pk=None):
        layers = NeuralNetwork.objects.get(pk=pk).neural_network_layers.all().values('name', 'index')
        return Response(layers, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=True)
    def predict(self, request, pk=None):
        pass


    # @action(methods=['post'], detail=True)
    # def activate(self, request, pk=None):

    #     current_active = NeuralNetwork.objects.filter(active=True)

    #     if len(current_active) == 1:
    #         current_active[0].active = False
    #         current_active[0].save()

    #     new_active = NeuralNetwork.objects.get(pk=pk)
    #     new_active.active = True
    #     new_active.save()

    #     return Response(status=status.HTTP_200_OK)