from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rest_framework import viewsets
from tasks.forms import TaskUpdateForm, TaskForm
from tasks.models import Task
from tasks.serializers import TaskSerializer, UserSerializer

# API Views
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Task.objects.filter(author=user)

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return User.objects.filter(username=user)

# Views
class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    ordering = ['-pk']

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset.filter(author=self.request.user)
        return queryset.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tasks'
        context['about_active'] = 'active'
        context['about_aria_current'] = 'page'
        return context

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'tasks/task_create.html'
    form_class = TaskForm
    login_url = 'login'
    redirect_to_login = 'tasks'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'tasks/task_update.html'
    form_class = TaskUpdateForm
    login_url = 'login'
    redirect_to_login = 'tasks'

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('tasks')
    login_url = 'login'
    redirect_to_login = 'tasks'