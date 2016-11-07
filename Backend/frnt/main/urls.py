from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf.urls import include

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^register/$', views.register_user, name='register'),
    #url(r'^accounts/login/$', auth_views.login),

    url('^', include('django.contrib.auth.urls')),
    url(r'^dashboard/$', views.dashboard, name='dashboard')
]