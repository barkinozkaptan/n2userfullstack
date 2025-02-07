from rest_framework import serializers

# tasks/serializers.py
from core_task.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'completed']