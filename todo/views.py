from django.contrib.auth.models import User
from rest_framework import viewsets
from todo.models import Todo
from todo.serializers import TodoSerializer, UserSerializer


# API Views
class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Todo.objects.filter(author=user)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return User.objects.filter(username=user)
