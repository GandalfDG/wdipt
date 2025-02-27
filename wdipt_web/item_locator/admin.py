from django.contrib import admin
from .models import GeoPlace, Room, StoragePlace, Item

admin.site.register((GeoPlace, StoragePlace, Item))

class StoragePlaceInline(admin.TabularInline):
    model = StoragePlace

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    
    inlines = [
        StoragePlaceInline
    ]