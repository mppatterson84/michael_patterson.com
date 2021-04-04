from django.urls import path

from .views import (
    HomePageView,
    AboutPageView,
    ProjectsPageView,
    BrowserPageView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('projects/', ProjectsPageView.as_view(), name='projects'),
    path('browser/', BrowserPageView.as_view(), name='browser'),
]
