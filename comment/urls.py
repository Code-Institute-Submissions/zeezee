from django.urls import path
from . import views

urlpatterns = [
    path('', views.comment, name='comment'),
    path('<int:comment_id>/', views.comment_list, name='comment_list'),
]