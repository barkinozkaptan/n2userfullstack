from django.db import models
from core_user.models import User  # Import User model

class Album(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="albums")
    title = models.CharField(max_length=255)

    def __str__(self):
        return f"Album: {self.title} (User: {self.user.username})"
