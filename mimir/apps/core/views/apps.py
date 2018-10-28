from django.apps import apps

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class AppListView(APIView):

    def get(self, request, pk=None):

        installed_apps = []

        for app in apps.get_app_configs():
            installed_apps.append(app)

        return Response(
            installed_apps,
            status=status.HTTP_200_OK)