from django.urls import path
from django.urls.conf import include
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
)
from users.forms import (
    BSAuthenticationForm, BSPasswordChangeForm
)
from users.views import DashboardView

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(template_name='registration/login.html', form_class=BSAuthenticationForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_change/', PasswordChangeView.as_view(template_name='registration/password_change_form.html', form_class=BSPasswordChangeForm), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
]