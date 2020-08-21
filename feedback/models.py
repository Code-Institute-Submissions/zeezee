from django.db import models
from django.utils import timezone
from django.shortcuts import render, redirect


# Create your models here.
class Comment(models.Model): 
    name = models.CharField(max_length=80) 
    email = models.EmailField() 
    body = models.TextField() 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    active = models.BooleanField(default=True) 
 
    class Meta: 
        ordering = ('created')
 


    