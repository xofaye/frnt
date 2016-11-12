from django.conf.urls import url
from django.conf.urls import include

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^register/$', views.register_user, name='register'),
    #url(r'^accounts/login/$', auth_views.login),

    url('^', include('django.contrib.auth.urls')),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^search/$', views.search_furniture, name='search'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^logout_success/$', views.logout_success, name='logout_success'),

]