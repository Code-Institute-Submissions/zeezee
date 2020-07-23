from django.db import models
from django.contrib import admin


class ContactForm(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField(max_length=200)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')

