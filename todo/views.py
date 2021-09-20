from django.contrib.auth.models import User
from rest_framework import filters, viewsets
from todo.models import Todo
from todo.serializers import TodoSerializer, UserSerializer


# API Views
class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['pk', 'created_at', 'due_by', 'completed']
    # ordering = ['pk']

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
