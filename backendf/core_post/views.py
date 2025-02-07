from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.cache import cache
import logging

from .models import Post
from .serializers import PostSerializer

logger = logging.getLogger(__name__)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request, *args, **kwargs):
        cached_posts = cache.get("all_posts")
        if cached_posts:
            logger.info("Fetching posts from Redis cache")
            return Response({"source": "redis", "data": cached_posts})

        logger.info("Fetching posts from Database")
        posts = self.get_queryset()
        serializer = self.get_serializer(posts, many=True)
        cache.set("all_posts", serializer.data, timeout=600)
        return Response({"source": "database", "data": serializer.data})

    def filter_queryset_by_key(self, filter_key, filter_value):
        return self.queryset.filter(**{filter_key: filter_value})

    @action(detail=False, methods=['get'], url_path='user/(?P<user_id>[^/.]+)')
    def posts_by_user(self, request, user_id=None):
        cache_key = f"user_posts_{user_id}"
        cached_posts = cache.get(cache_key)

        if cached_posts:
            logger.info(f"Fetching posts for user {user_id} from Redis cache")
            return Response({"source": "redis", "data": cached_posts})

        logger.info(f"Fetching posts for user {user_id} from Database")
        queryset = self.filter_queryset_by_key('user_id', user_id)
        serializer = self.get_serializer(queryset, many=True)
        cache.set(cache_key, serializer.data, timeout=600)
        return Response({"source": "database", "data": serializer.data})
