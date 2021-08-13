from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class BSAuthenticationForm(AuthenticationForm):
    """
    Extend base class with Bootstrap styling.
    """
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}),
    )
