from django.contrib import admin
from django.urls import path

from .views import email_view, SuccessPageView

urlpatterns = [
    path('contact/', email_view, name='contact'),
    path('success/', SuccessPageView.as_view(), name='success'),
]