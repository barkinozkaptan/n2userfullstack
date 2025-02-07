

import logging
from django.core.cache import cache
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

# Import your User model and serializer
from .models import User
from .serializers import UserSerializer
from throttling import RedisRateThrottle  # adjust if necessary

logger = logging.getLogger(__name__)

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for listing, retrieving, and managing users.
    The list endpoint now returns a wrapped response with a "source" and "data" keys.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    throttle_classes = [RedisRateThrottle]

    def list(self, request, *args, **kwargs):
        try:
            # Try to get cached data first
            cached_users = cache.get("all_users")
            if cached_users:
                logger.info("✅ Fetching users from Redis cache")
                return Response({"source": "redis", "data": cached_users})

            # Otherwise, query the database and serialize the data
            logger.info("📌 Fetching users from Database")
            users = self.get_queryset()
            serializer = self.get_serializer(users, many=True)
            # Cache the serialized data for 10 minutes
            cache.set("all_users", serializer.data, timeout=600)
            return Response({"source": "database", "data": serializer.data})
        except Exception as e:
            logger.error(f"❌ Error fetching users: {str(e)}")
            return Response({"error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
