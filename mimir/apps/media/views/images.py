from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Image
from ..serializers import ImageSerializer

class ImageListView(APIView):

    def get(self, request, pk=None):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK)

    def post(self, request):

        serializer = ImageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ImageView(APIView):

    def get(self, request, pk=None):
        image = Image.objects.get(pk=pk)
        serializer = ImageSerializer(image)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK)