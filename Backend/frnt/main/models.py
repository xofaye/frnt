import os
from django.db import models
from django.contrib.auth.models import User


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


class Location(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=15)
    street_address = models.CharField(max_length=100)


class FrnTUser(models.Model):
    '''
    User:
        username
        password
        first_name
        last_name
        email
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.OneToOneField('Location', blank=True)
    profile_image = models.ImageField(upload_to=get_image_path, blank=True)
    biography = models.CharField(max_length=500, blank=True)
    rating = models.DecimalField(default=0, max_digits=3, decimal_places=2)
    rating_count = models.IntegerField(default=0)


class FrnTListing(models.Model):
    user = models.ForeignKey('FrnTUser', unique=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)
    picture = models.ImageField(upload_to=get_image_path, blank=True)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    location = models.OneToOneField('Location')
