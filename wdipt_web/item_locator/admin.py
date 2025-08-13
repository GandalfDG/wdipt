from django.contrib import admin
from .models import GeoPlace, Room, StoragePlace, Item

admin.site.register((GeoPlace, Item))

class StoragePlaceInline(admin.TabularInline):
    model = StoragePlace

class ItemInline(admin.TabularInline):
    model = Item

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    
    inlines = [
        StoragePlaceInline
    ]

@admin.register(StoragePlace)
class StorageAdmin(admin.ModelAdmin):

    inlines = [
        ItemInline
    ]