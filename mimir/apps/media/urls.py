from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    # ex: /media/
    path('images/', views.image_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)