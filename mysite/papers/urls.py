from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url('paperlist', views.paperlist, name = 'paperlist'),
    url('papercontent', views.papercontent, name = 'papercontent'),
    url('annotation', views.paperannotation, name= 'annotation'),
    # url('contentdemo', views.contentdemo, name = 'contentdemo'),
]
