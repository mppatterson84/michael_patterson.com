from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    UsernameField
)


class BSAuthenticationForm(AuthenticationForm):
    """
    Extend AuthenticationForm base class with Bootstrap styling.
    """
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}),
    )

class BSPasswordChangeForm(PasswordChangeForm):
    """
    Extend PasswordChangeForm base class with Bootstrap styling.
    """
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True, 'class': 'form-control'}),
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
    )