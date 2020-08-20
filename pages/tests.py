from django.test import TestCase
from .views import about, contact, success

# Create your tests here.
class TestPagesViews(TestCase):

    def test_about_load(self):
        response = self.client.get('/about')
        self.assertTemplateUsed( 'pages/about.html')

    def test_contact_load(self):
        response = self.client.get('/contact')
        self.assertTemplateUsed( 'pages/contact.html')
    
    def test_success_load(self):
        response = self.client.get('/success')
        self.assertTemplateUsed( 'pages/success-contact.html')
