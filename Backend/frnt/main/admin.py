from django.contrib import admin

# Register your models here.

from .models import User, Location, Listing

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    pass
