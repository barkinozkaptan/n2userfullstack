from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from django.core.cache import cache
import logging

from .models import Task
from .serializers import TaskSerializer

logger = logging.getLogger(__name__)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # Replicate the logic from BaseViewSet:
    def filter_queryset_by_key(self, filter_key, filter_value):
        return self.queryset.filter(**{filter_key: filter_value})

    @action(detail=False, methods=['get'], url_path='user/(?P<user_id>[^/.]+)')
    def tasks_by_user(self, request, user_id=None):
        cache_key = f"user_tasks_{user_id}"
        cached_tasks = cache.get(cache_key)

        if cached_tasks:
            logger.info(f"✅ Fetching tasks for user {user_id} from Redis cache")
            return Response({"source": "redis", "data": cached_tasks})

        logger.info(f"📌 Fetching tasks for user {user_id} from Database")
        queryset = self.filter_queryset_by_key('user_id', user_id)
        serializer = self.get_serializer(queryset, many=True)

        # ✅ Store user-specific tasks in Redis before returning
        cache.set(cache_key, serializer.data, timeout=600)
        return Response({"source": "database", "data": serializer.data})

    def update(self, request, *args, **kwargs):
        task = self.get_object()
        response = super().update(request, *args, **kwargs)

        # ✅ Clear and update Redis cache for the user
        user_id = task.user.id
        cache_key = f"user_tasks_{user_id}"
        updated_tasks = Task.objects.filter(user_id=user_id)
        serializer = self.get_serializer(updated_tasks, many=True)

        cache.set(cache_key, serializer.data, timeout=600)  # ✅ Refresh cache after update
        logger.info(f"♻️ Redis cache updated for user {user_id} tasks")

        return response


@api_view(['GET', 'PUT'])
def user_tasks(request, user_id):
    """
    Separate function-based view for fetching/updating tasks by user.
    """
    if request.method == 'GET':
        tasks = Task.objects.filter(user_id=user_id)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        updated_tasks = request.data.get('todos', [])

        for task_data in updated_tasks:
            try:
                task = Task.objects.get(id=task_data["id"], user_id=user_id)
                serializer = TaskSerializer(task, data=task_data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Task.DoesNotExist:
                return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"message": "Tasks updated successfully"}, status=status.HTTP_200_OK)
