from django.conf.urls import url
from django.conf.urls import include

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url('^', include('django.contrib.auth.urls')),

    url(r'^register/$', views.register_user, name='register'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^(?P<username>[\d]+)/', include([
        url(r'^$', views.view_profile, name='view_profile'),
    ])),
    url(r'^logout_success/$', views.logout_success, name='logout_success'),
    
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^search/$', views.search_furniture, name='search'),

    url(r'^listing/add$', views.add_listing, name='add_listing'),
    url(r'^listing/edit$', views.edit_listing, name='edit_listing'),
    url(r'^listing/(?P<id>[\d]+)/', include([
        url(r'^$', views.view_listing, name='view_listing'),
    ])),
]