from django.urls import path
from rest_framework.routers import SimpleRouter
from tasks.views import UserViewSet, TaskViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('api/tasks/v1', TaskViewSet, basename='tasks')

urlpatterns = router.urls
