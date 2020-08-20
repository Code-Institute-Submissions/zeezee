from django.test import TestCase
from .views import view_bag, add_to_cart, remove_from_cart

# Create your tests here.
class TestProductViews(TestCase):

    def test_view_bag_view(self):
        response = self.client.get('/')
        self.assertTemplateUsed( 'bag/bag.html')
    
    def test_add_to_cart(self):
        response = self.client.get('add/<item_id>/')
        
    def test_remove_from_cart(self):
        response = self.client.get('remove/<item_id>/')
        