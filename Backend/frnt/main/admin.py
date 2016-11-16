from django.contrib import admin

# Register your models here.

from .models import Profile, Location, Listing, ListingPicture

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    pass

@admin.register(ListingPicture)
class ListingPictureAdmin(admin.ModelAdmin):
    pass
