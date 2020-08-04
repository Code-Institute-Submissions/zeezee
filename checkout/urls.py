from django.urls import path
from . import views

'''
Path for checkout
'''

urlpatterns = [
    path('', views.checkout, name='checkout')
]
