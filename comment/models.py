from django.db import models
from django.shortcuts import render, redirect


# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=80, blank=False) 
    email = models.EmailField(blank=False) 
    body = models.TextField(blank=False) 
    created = models.DateTimeField(auto_now_add=True, blank=False) 
    updated = models.DateTimeField(auto_now=True, blank=False) 
    active = models.BooleanField(default=True, blank=False) 

