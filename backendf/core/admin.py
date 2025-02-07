from django.contrib import admin
from core_user.models import User
from core_post.models import Post
from core_comment.models import Comment
from core_album.models import Album
from core_photo.models import Photo
from core_task.models import Task

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Album)
admin.site.register(Photo)
admin.site.register(Task)
