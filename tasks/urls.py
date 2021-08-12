from django.urls import path
from rest_framework.routers import SimpleRouter
from tasks.views import (
    TaskViewSet,
    UserViewSet,
    TaskListView,
    TaskCreateView,
)

router = SimpleRouter()
router.register('api/tasks/v1/users', UserViewSet, basename='users')
router.register('api/tasks/v1', TaskViewSet, basename='tasks')


urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='tasks'),
    path('tasks/add/', TaskCreateView.as_view(), name='tasks-add'),
] + router.urls
