from django import forms
from django.core.mail import send_mail


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    your_email = forms.EmailField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
