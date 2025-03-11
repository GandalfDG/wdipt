from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse
from django.forms import inlineformset_factory

from .models import StoragePlace, Room, GeoPlace, Item
from .forms import ItemForm

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
    
class StoragePlaceCatalogItemsView(View):
    """When I'm in front of a storage place, allow me to catalog the items in it
    through an item formset.
    
    Show the existing items in the place, and present forms to allow adding one or
    more items at once.
    """
    ItemInlineFormSet = inlineformset_factory(StoragePlace, Item, ItemForm)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def get(self, request, pk):
        place_instance = StoragePlace.objects.get(pk=pk)
        formset = self.ItemInlineFormSet(instance=place_instance)
        return HttpResponse(formset)
