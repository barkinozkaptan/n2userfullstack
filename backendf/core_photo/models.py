from django.db import models
from core_album.models import Album  # Import the Album model

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="photos")
    title = models.CharField(max_length=255)
    url = models.URLField()
    thumbnail_url = models.URLField()

    def __str__(self):
        return f"Photo: {self.title} (Album: {self.album.id})"
