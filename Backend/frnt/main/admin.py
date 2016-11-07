from django.contrib import admin

# Register your models here.

from .models import FnrtUser, Location, FnrtListing

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass

@admin.register(FnrtUser)
class FnrtUserAdmin(admin.ModelAdmin):
    pass

@admin.register(FnrtListing)
class FnrtListingAdmin(admin.ModelAdmin):
    pass
