from django.urls import path
from django.urls.conf import include
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,
    PasswordResetCompleteView
)
from users.forms import (
    BSAuthenticationForm, BSPasswordChangeForm, BSPasswordResetForm,
    BSSetPasswordForm
)
from users.views import DashboardView, RegisterView

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(template_name='registration/login.html', form_class=BSAuthenticationForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_change/', PasswordChangeView.as_view(template_name='registration/password_change_form.html', form_class=BSPasswordChangeForm), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(template_name='registration/password_reset_form.html', form_class=BSPasswordResetForm), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html', form_class=BSSetPasswordForm), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('signup/', RegisterView.as_view(), name='signup'),
]