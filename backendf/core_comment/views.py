from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.cache import cache
import logging

from .models import Comment
from .serializers import CommentSerializer

logger = logging.getLogger(__name__)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def filter_queryset_by_key(self, filter_key, filter_value):
        return self.queryset.filter(**{filter_key: filter_value})

    @action(detail=False, methods=['get'], url_path='post/(?P<post_id>[^/.]+)')
    def comments_by_post(self, request, post_id=None):
        cache_key = f"post_comments_{post_id}"
        cached_comments = cache.get(cache_key)

        if cached_comments:
            logger.info(f"Fetching comments for post {post_id} from Redis cache")
            return Response({"source": "redis", "data": cached_comments})

        logger.info(f"Fetching comments for post {post_id} from Database")
        queryset = self.filter_queryset_by_key('post_id', post_id)
        serializer = self.get_serializer(queryset, many=True)
        cache.set(cache_key, serializer.data, timeout=600)
        return Response({"source": "database", "data": serializer.data})
