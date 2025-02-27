from django.contrib import admin
from .models import GeoPlace, Room, StoragePlace, Item

admin.site.register((GeoPlace, Room, StoragePlace, Item))
# Register your models here.
