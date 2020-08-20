from django.test import TestCase
from .views import index

# Test if the homepage is rendered correctly using the template

class TestHomeViews(TestCase):

    def test_home_page(self):
        response = self.client.get('/')
        self.assertTemplateUsed( 'home/index.html')
