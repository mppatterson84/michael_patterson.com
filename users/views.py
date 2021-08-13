from django.contrib.messages.views import SuccessMessageMixin
from django.urls.base import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from users.forms import BSUserCreationForm

class DashboardView(TemplateView):
    template_name = 'users/dashboard.html'

class RegisterView(SuccessMessageMixin, CreateView):
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')
    form_class = BSUserCreationForm
    success_message = 'User was created successfully.'
