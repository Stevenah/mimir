from django.urls import path

from . import views

urlpatterns = [
    # ex: /reporting/
    path('', views.index, name='index'),
]