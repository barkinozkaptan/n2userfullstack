from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core_user.views import UserViewSet
from core_post.views import PostViewSet
from core_comment.views import CommentViewSet
from core_album.views import AlbumViewSet
from core_photo.views import PhotoViewSet
from core_task.views import TaskViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'photos', PhotoViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
