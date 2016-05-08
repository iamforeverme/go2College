from django.conf.urls import include, url

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, {'template_name': 'login/login.html'}),
    url(r'^profile/$', views.profile),
    url('', include('django.contrib.auth.urls')),
]