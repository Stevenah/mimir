from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import NeuralNet
from ..serializers import NeuralNetSerializer

class NeuralNetListView(APIView):

    def get(self, request, pk=None):
        nets = NeuralNet.objects.all()
        serializer = NeuralNetSerializer(nets, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK)

class NeuralNetView(APIView):
    
    def get(self, request, pk=None):
        net = NeuralNet.objects.get(pk=pk)
        serializer = NeuralNetSerializer(net)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK)