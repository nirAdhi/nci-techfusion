from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index1, name='index1'),
    re_path(r'^login/$', views.login, name='login'),
    re_path(r'^home/$', views.home, name='home'),
]