from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.cache import cache
import logging

from .models import Album
from .serializers import AlbumSerializer

logger = logging.getLogger(__name__)

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def filter_queryset_by_key(self, filter_key, filter_value):
        return self.queryset.filter(**{filter_key: filter_value})

    @action(detail=False, methods=['get'], url_path='user/(?P<user_id>[^/.]+)')
    def albums_by_user(self, request, user_id=None):
        cache_key = f"user_albums_{user_id}"
        cached_albums = cache.get(cache_key)

        if cached_albums:
            logger.info(f"Fetching albums for user {user_id} from Redis cache")
            return Response({"source": "redis", "data": cached_albums})

        logger.info(f"Fetching albums for user {user_id} from Database")
        queryset = self.filter_queryset_by_key('user_id', user_id)
        serializer = self.get_serializer(queryset, many=True)
        cache.set(cache_key, serializer.data, timeout=600)
        return Response({"source": "database", "data": serializer.data})
