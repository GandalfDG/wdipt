from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView

from .models import StoragePlace, Room, GeoPlace, Item

# Create your views here.
class GeoPlaceDetailView(DetailView):
    """Present all of the rooms in a place"""
    model = GeoPlace
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rooms"] = self.object.room_set.all()
        return context

class RoomDetailView(DetailView):
    """Present all of the storage places in a room"""
    model = Room
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["storage_places"] = self.object.storageplace_set.all()
        return context
    
class StoragePlaceDetailView(DetailView):
    """Present all of the items in a storage place"""
    model = StoragePlace
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["items"] = self.object.item_set.all()
        return context

class StoragePlaceCreateView(CreateView):
    model = StoragePlace
    fields = ["name", "description", "room"]
    
class StoragePlaceCatalogItemsView():
    pass
