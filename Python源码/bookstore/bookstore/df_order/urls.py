from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('^$', views.order, name='order'),
    path('addorder/', views.addorder, name='addorder'),
    re_path('^pay/(\d+)$', views.pay, name='pay'),
]