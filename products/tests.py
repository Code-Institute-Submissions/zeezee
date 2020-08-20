from django.test import TestCase
from .models import Product
from .views import all_products, edit_product, add_new_product, delete_product, detail_product



class TestProductViews(TestCase):

    def test_all_product_view(self):
        response = self.client.get('/products')
        self.assertTemplateUsed( 'products/products.html')

    def test_edit_product(self):
        response = self.client.get('/products/edit/<int:product_id>/')
        self.assertTemplateUsed( 'products/edit_product.html')

    def test_delete_product(self):
        response = self.client.get('/products/delete/<int:product_id>/')
        self.assertTemplateUsed( 'products/products.html')

    def test_delete_product(self):
        response = self.client.get('/products/delete/<int:product_id>/')
        self.assertTemplateUsed( 'products/products.html')
    
    def test_detail_product(self):
        response =self.client.get('<int:product_id>/')
        self.assertTemplateUsed('products/detail_product.html')
    
    