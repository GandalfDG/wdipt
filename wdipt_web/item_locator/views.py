from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView

from .models import StoragePlace

# Create your views here.
class StorageCatalogView(CreateView):
    model = StoragePlace
