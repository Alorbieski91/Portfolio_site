import os

from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

from .forms import ContactForm

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

class ProjectsView(TemplateView):
    template_name = "projects.html"

class AboutView(TemplateView):
    template_name = "about.html"

class ContactMeView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = '/contactme/thanks'

    def form_valid(self, form):
        self.send_email(form.cleaned_data)

        return super(ContactMeView, self).form_valid(form)

    def send_email(self, valid_data):
        subject = valid_data['subject']
        your_email = valid_data['your_email']
        message = valid_data['your_email'] + '\n'*2 + valid_data['message']

        
        send_mail(subject, message, your_email, [os.environ.get('EMAIL_HOST_USER')])

        print('Email sent')

class EmailSentView(TemplateView):
    template_name = "thanks.html"