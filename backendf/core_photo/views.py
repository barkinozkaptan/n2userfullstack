from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.cache import cache
import logging

from .models import Photo
from .serializers import PhotoSerializer

logger = logging.getLogger(__name__)

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def filter_queryset_by_key(self, filter_key, filter_value):
        return self.queryset.filter(**{filter_key: filter_value})

    @action(detail=False, methods=['get'], url_path='album/(?P<album_id>[^/.]+)')
    def photos_by_album(self, request, album_id=None):
        cache_key = f"album_photos_{album_id}"
        cached_photos = cache.get(cache_key)

        if cached_photos:
            logger.info(f"Fetching photos for album {album_id} from Redis cache")
            return Response({"source": "redis", "data": cached_photos})

        logger.info(f"Fetching photos for album {album_id} from Database")
        queryset = self.filter_queryset_by_key('album_id', album_id)
        serializer = self.get_serializer(queryset, many=True)
        cache.set(cache_key, serializer.data, timeout=600)
        return Response({"source": "database", "data": serializer.data})
