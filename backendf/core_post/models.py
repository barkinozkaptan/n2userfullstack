from django.db import models
from core_user.models import User  # Import User model

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title
