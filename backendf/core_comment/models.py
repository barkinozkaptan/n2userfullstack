from django.db import models
from core_post.models import Post  # Import Post model

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return f"Comment by {self.name} on {self.post.title}"
