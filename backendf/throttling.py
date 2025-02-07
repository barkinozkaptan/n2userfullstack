from rest_framework.throttling import BaseThrottle
from django.core.cache import cache

class RedisRateThrottle(BaseThrottle):
    def allow_request(self, request, view):
        user_ip = request.META.get('REMOTE_ADDR')
        key = f"rate_limit:{user_ip}"
        requests_count = cache.get(key, 0)

        if requests_count >= 500:
            return False  # Block request

        cache.set(key, requests_count + 1, timeout=60)
        return True
