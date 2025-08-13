from django.urls import path

from .views import ItemDetailView, StoragePlaceDetailView, StoragePlaceCreateView, RoomDetailView, GeoPlaceDetailView, StoragePlaceCatalogItemsView

urlpatterns = [
    path("storage/", StoragePlaceCreateView.as_view()),
    path("storage/<int:pk>", StoragePlaceDetailView.as_view()),
    path("room/<int:pk>", RoomDetailView.as_view()),
    path("place/<int:pk>", GeoPlaceDetailView.as_view()),
    path("item/<int:pk>", ItemDetailView.as_view()),
    path("storage/catalog/<int:pk>", StoragePlaceCatalogItemsView.as_view(), name="catalog"),
]