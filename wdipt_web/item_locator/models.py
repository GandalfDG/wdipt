from django.db import models

class CommonModel(models.Model):
    
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        abstract = True

class GeoPlace(CommonModel):
    
    class Meta:
        verbose_name = "geographic location"
    
class Room(CommonModel):
    geo_place = models.ForeignKey(to=GeoPlace, on_delete=models.SET_NULL, null=True)

class StoragePlace(CommonModel):
    room = models.ForeignKey(to=Room, on_delete=models.SET_NULL, null=True)
    
class Item(CommonModel):
    place = models.ForeignKey(to=StoragePlace, on_delete=models.SET_NULL, null=True)