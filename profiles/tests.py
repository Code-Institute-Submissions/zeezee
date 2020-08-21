from django.test import TestCase
from .views import profile, order_history


# Create your tests here.
class TestProfileView(TestCase):

    def test_profile_view(self):
        response = self.client.get('/')
        self.assertTemplateUsed('profiles/profile.html')

    def test_order_history_view(self):
        response = self.client.get('/order_history/<order_number>')
        self.assertTemplateUsed('checkout/checkout_success.html')


