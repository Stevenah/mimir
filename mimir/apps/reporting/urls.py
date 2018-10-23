from django.urls import path, re_path

from . import views

urlpatterns = [
    
    # catch-all
    re_path(r'^(?P<path>.*)/$', views.index, name='index'),

    # ex: /reporting/
    path('', views.index, name='index'),
]