from django.contrib import admin
from django.urls import path

from .views import EmailContactView, SuccessPageView

urlpatterns = [
    path('contact/', EmailContactView.as_view(), name='contact'),
    path('success/', SuccessPageView.as_view(), name='success'),
]