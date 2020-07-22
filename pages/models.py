from django.db import models
from django.contrib import admin
from django import forms
from .models import Contact


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()

class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField(max_length=10) 
    

