from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('^$', views.cart, name='cart'),
    re_path('^add(\d+)_(\d+)$', views.add, name='add'),
    re_path('^edit(\d+)_(\d+)$', views.edit, name='edit'),
    re_path('^delete(\d+)$', views.delete, name='delete'),
]
