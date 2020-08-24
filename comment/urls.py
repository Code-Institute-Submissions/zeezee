from django.urls import path
from . import views

urlpatterns = [
    path('', views.comment, name='comment'),
    path('list', views.comment_list, name='comment_list'),
]