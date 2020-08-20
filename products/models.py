from django.db import models

# Create your models here.
# Base of the models from the Boutique Ado project


class Category(models.Model):
    '''
    Categories with a name and a friendly name for frontend
    Both of them have max lenght,
    the friendly name it's not required (because blank=True)
    Metaclass provided to fix the spelling,
    declare that the plural version of Category is not Categorys
    '''

    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    '''
    Product model with key elements
    Category, sku, image url and image fields are optional
    '''
    category = models.ForeignKey('Category', null=True, blank=False, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=False)
    name = models.CharField(max_length=254, blank=False)
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False) 
    image1 = models.ImageField(null=True, blank=False)
    image2 = models.ImageField(null=True, blank=False)

    def __str__(self):
        return self.name
