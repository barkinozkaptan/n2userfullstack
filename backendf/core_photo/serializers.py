from rest_framework import serializers

# photos/serializers.py
from core_photo.models import Photo

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'album', 'title', 'url', 'thumbnail_url']