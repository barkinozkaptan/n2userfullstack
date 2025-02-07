from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from core_task.views import user_tasks

urlpatterns = [
    path('admin/', admin.site.urls),               # Admin panel
    path('api/', include('core.urls')),            # API endpoints (using 'core/urls.py')
    path('api-auth/', include('rest_framework.urls')),  # DRF Auth endpoints
    path('', TemplateView.as_view(template_name="index.html")),  # Serve Vue.js app
    path('api/tasks/user/<int:user_id>/', user_tasks, name='user_tasks'),
]
