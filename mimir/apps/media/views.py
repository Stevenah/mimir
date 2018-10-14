from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.decorators import renderer_classes

from .models import Image
from .serializers import ImageSerializer

import PIL
import io

from django.core.files.base import ContentFile
from django.core.files.images import ImageFile

@api_view(['GET', 'POST'])
@renderer_classes((JSONRenderer,))
def image_list(request):
    """
    List all code snippets, or create a new snippet.
    """

    print(request.method)

    if request.method == 'GET':
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        serializer = ImageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)