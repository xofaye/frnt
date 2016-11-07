from django.contrib import admin

# Register your models here.

from .models import FrnTUser, Location, FrnTListing

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass

@admin.register(FrnTUser)
class FrnTUserAdmin(admin.ModelAdmin):
    pass

@admin.register(FrnTListing)
class FrnTListingAdmin(admin.ModelAdmin):
    pass
