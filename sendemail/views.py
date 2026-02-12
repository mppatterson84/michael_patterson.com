import os
import requests

from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import EmailForm


class EmailContactView(TemplateView):
    form_class = EmailForm
    template_name = 'sendemail/email.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': os.environ['RECAPTCHA_SECRET_KEY_V2'],
                'response': recaptcha_response
            }
            r = requests.post(
                'https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()
            email = EmailMessage(
                subject=form.cleaned_data['subject'],
                body=form.cleaned_data['message'],
                from_email=os.environ['SEND_EMAIL_ADDRESS'],
                to=[os.environ['EMAIL_HOST_USER']],
                reply_to=[form.cleaned_data['from_email']]
            )
            # subject = form.cleaned_data['subject']
            # from_email = os.environ['EMAIL_HOST_USER']
            # user_email_address = form.cleaned_data['from_email']
            # message = f"Someone sent a message from the contact form at michael-patterson.com\nsender email: {user_email_address}\n{form.cleaned_data['message']}"
            if result['success']:
                form.save()
                try:
                    # send_mail(subject, message, from_email, [os.environ['SEND_EMAIL_ADDRESS']])
                    email.send()
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
            else:
                messages.error(
                    request, 'Invalid reCAPTCHA. Please try again.', extra_tags='alert alert-warning')
                return redirect('contact')
            return redirect('success')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact'
        context['contact_active'] = 'active'
        context['contact_aria_current'] = 'page'
        context['reCAPTCHA_site_key_v2'] = os.environ.get('RECAPTCHA_SITE_KEY_V2')
        context['form'] = self.form_class
        return context
    

class SuccessPageView(TemplateView):
    template_name = 'sendemail/success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Success'
        return context
