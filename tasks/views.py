from django.contrib.auth import get_user_model
from rest_framework import viewsets
from tasks.models import Task
from tasks.permissions import IsUserOrReadOnly
from tasks.serializers import TaskSerializer, UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (IsUserOrReadOnly,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer    
