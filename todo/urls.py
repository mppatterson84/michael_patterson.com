from django.urls import path, include
from rest_framework.routers import SimpleRouter
from todo.views import (
    TodoViewSet,
    UserViewSet,
)

router = SimpleRouter()
router.register('api/todos/v1/users', UserViewSet, basename='users')
router.register('api/todos/v1', TodoViewSet, basename='todos')


urlpatterns = [
#     path('api/todos/v1/rest-auth/', include('rest_auth.urls')),
#     path('api/todos/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
] + router.urls
