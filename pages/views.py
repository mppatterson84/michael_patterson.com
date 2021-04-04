from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
import os
from pages.utils import get_cloudinary_timestamp, get_cloudinary_signature


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        context['home_active'] = 'active'
        context['home_active_link'] = '#'
        context['home_active_sr'] = '<span class="sr-only">(current)</span>'
        return context


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About'
        context['about_active'] = 'active'
        context['about_active_link'] = '#'
        context['about_active_sr'] = '<span class="sr-only">(current)</span>'
        return context


class ProjectsPageView(TemplateView):
    template_name = 'pages/projects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Projects'
        context['projects_active'] = 'active'
        context['projects_active_link'] = '#'
        context['projects_active_sr'] = '<span class="sr-only">(current)</span>'
        return context


class BrowserPageView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/browser.html'
    login_url = '/admin/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Browser'
        context['browser_active'] = 'active'
        context['browser_active_link'] = '#'
        context['browser_active_sr'] = '<span class="sr-only">(current)</span>'
        context['cloud_name'] = os.environ.get('CLOUD_NAME')
        context['api_key'] = os.environ.get('API_KEY')
        context['user_name'] = os.environ.get('CLOUDINARY_USER')
        context['signature'] = get_cloudinary_signature()
        context['timestamp'] = get_cloudinary_timestamp()
        return context
