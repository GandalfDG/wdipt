from django import forms
from .models import Room, StoragePlace, Item

class RoomForm(forms.ModelForm):
    
    class Meta:
        model = Room
        fields = ["name", "description", "geo_place"]

class StoragePlaceForm(forms.ModelForm):
    
    class Meta:
        model = StoragePlace
        fields = ["name", "description", "room"]
        
class ItemForm(forms.ModelForm):
    
    class Meta:
        model = Item
        fields = ["name", "description", "place"]

class ItemCatalogForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ["name", "description"]