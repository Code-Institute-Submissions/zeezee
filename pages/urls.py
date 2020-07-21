from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('about_view', views.about_view, name='about'),

]
