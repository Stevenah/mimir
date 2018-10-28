from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.renderers import JSONRenderer

from ..models import Application
from .. import serializers


class ApplicationsViewSet(viewsets.ModelViewSet):
    renderer_classes = (JSONRenderer, )
    serializer_class = serializers.ApplicationSerializer
    queryset = Application.objects.all()