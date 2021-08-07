from rest_framework import generics
from tasks.models import Task
from tasks.permissions import IsUserOrReadOnly
from tasks.serializers import TaskSerializer

class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsUserOrReadOnly,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer