from rest_framework import serializers

# albums/serializers.py
from core_album.models import Album

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'user', 'title']