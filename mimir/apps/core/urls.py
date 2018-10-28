from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from . import viewsets

router = DefaultRouter()

router.register('apps', viewsets.ApplicationsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]