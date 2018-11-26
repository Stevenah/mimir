from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status

from django_filters.rest_framework import DjangoFilterBackend

from keras.models import load_model

from ..serializers import NeuralNetSerializer
from ..models import NeuralNet
from .. import serializers

class NeuralNetViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.NeuralNetSerializer
    queryset = NeuralNet.objects.all()
    renderer_classes = (JSONRenderer, )
    filter_backends = (DjangoFilterBackend, )
    
    @action(methods=['get'], detail=True)
    def classes(self, request, pk=None):

        classes = NeuralNet.objects.get(pk=pk).dataset.dataset_categories.all()
        serializer = serializers.DatasetCategoriesSerializer(classes, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=True)
    def predict(self, request, pk=None):
        pass





    # @action(methods=['post'], detail=True)
    # def activate(self, request, pk=None):

    #     current_active = NeuralNet.objects.filter(active=True)

    #     if len(current_active) == 1:
    #         current_active[0].active = False
    #         current_active[0].save()

    #     new_active = NeuralNet.objects.get(pk=pk)
    #     new_active.active = True
    #     new_active.save()

    #     return Response(status=status.HTTP_200_OK)