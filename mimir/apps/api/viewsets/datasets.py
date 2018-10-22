from rest_framework import viewsets, permissions
from ..models import Dataset
from .. import serializers

class DatasetViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DatasetSerializer
    queryset = Dataset.objects.all()