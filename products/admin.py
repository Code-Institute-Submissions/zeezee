from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    '''Product info in ProductAdmin'''
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image1',
        'image2',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

# Register classes with models

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)