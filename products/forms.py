from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        '''
        Metaclass defining the model and the fields
        we want to use in ProductForm
        Product model and all the fields included
        '''
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        '''
        The superuser is able to add, edit and delete things
        Categories displayed with their friendly names
        Display field item with the matching styling attribute
        '''
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'purple-text'
