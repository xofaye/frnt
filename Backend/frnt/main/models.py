import os
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


class Location(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=15)
    street_address = models.CharField(max_length=100)


class Profile(models.Model):
    '''
    User:
        username
        password
        first_name
        last_name
        email
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    location = models.ForeignKey('Location', blank=True, null=True)
    profile_image = models.ImageField(upload_to=get_image_path, blank=True)
    biography = models.CharField(max_length=500, blank=True)
    rating = models.DecimalField(default=0, max_digits=3, decimal_places=2)
    rating_count = models.IntegerField(default=0)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Listing(models.Model):
    user = models.ForeignKey('Profile')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)
    picture = models.ImageField(upload_to=get_image_path, blank=True)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    location = models.OneToOneField('Location')
