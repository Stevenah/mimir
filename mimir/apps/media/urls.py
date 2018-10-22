from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

from . import viewsets

router = DefaultRouter()

router.register('neural', viewsets.NeuralNetViewSet)
router.register('images', viewsets.ImageViewSet)
router.register('datasets', viewsets.DatasetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = format_suffix_patterns(urlpatterns)