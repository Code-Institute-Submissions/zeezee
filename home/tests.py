from django.test import TestCase
from .views import index

# Create your tests here.

class TestHomeViews(TestCase):

    def test_home_page(self):
        response = self.client.get('/')
        self.assertTemplateUsed( 'home/index.html')
