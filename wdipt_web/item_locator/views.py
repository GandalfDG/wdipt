from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView

from .models import StoragePlace, Room, Item

# Create your views here.
class RoomDetailView(DetailView):
    model = Room
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["storage_places"] = self.get_object().storageplace_set.all()
        return context
    
class StoragePlaceDetailView(DetailView):
    model = StoragePlace
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["items"] = self.get_object().item_set.all()
        return context

class StoragePlaceCreateView(CreateView):
    model = StoragePlace
    fields = ["name", "description", "room"]
    
class StoragePlaceCatalogItemsView():
    pass
