from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.detail_product, name='detail_product'),
    path('add/', views.add_new_product, name='add_new_product'),
]