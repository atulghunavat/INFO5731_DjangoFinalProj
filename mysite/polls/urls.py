from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^paperlist/$', views.paperlist, name = 'paperlist'),
    url(r'^papercontent/$', views.papercontent, name = 'papercontent'),
    url(r'^paperannotation/$', views.paperannotation, name= 'annotation'),
]