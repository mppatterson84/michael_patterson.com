from django.urls import path
from django.urls.conf import include
from django.contrib.auth.views import LoginView, LogoutView
from users.forms import BSAuthenticationForm
from users.views import DashboardView

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(template_name='registration/login.html', authentication_form=BSAuthenticationForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]