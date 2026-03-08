from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('^register$', views.register, name='register'),
    re_path('^register_handle$', views.register_handle, name='register_handle'),
    re_path('^register_exist$', views.register_exist, name='register_exist'),
    re_path('^login/$', views.login, name='login'),
    re_path('^login_handle$', views.login_handle, name='login_handle'),
    re_path('^info$', views.info, name='info'),
    re_path('^order/(\d*)$', views.order, name='order'),
    re_path('^site$', views.site, name='site'),
    re_path('^logout$', views.logout, name='logout'),
    re_path('^verifyCode$', views.verifyCode, name="verifyCode"),
    re_path('^verifyTest$', views.verifyTest, name="verifyTest"),
    re_path('^verifyTest2$', views.verifyTest2, name="verifyTest2"),
]