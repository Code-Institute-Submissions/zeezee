from django.test import TestCase
from .views import checkout_success

class TestCheckoutViews(TestCase):

    def test_checkout_success(self):
        response = self.client.get('/checkout_success/<order_number>')
        self.assertTemplateUsed( 'checkout/checkout_success.html')