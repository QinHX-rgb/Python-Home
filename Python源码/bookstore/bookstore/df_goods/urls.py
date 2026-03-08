from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('^index$', views.index, name='index'),
    re_path('^list(\d+)_(\d+)_(\d+)$', views.list, name='list'),
    re_path('^(\d+)$', views.detail, name='detail'),
]

