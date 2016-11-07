from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^register/$', views.register_user, name='register'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
]