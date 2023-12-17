from django.forms import ModelForm
from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'brand', 'image', 'price', 'quantity', 'description']
