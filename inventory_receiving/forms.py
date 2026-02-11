from django import forms
from django.forms import inlineformset_factory
from .models import ProductType, Product, ProductImage


class ProductTypeForm(forms.ModelForm):
    """Form for creating and editing Product Types."""
    
    class Meta:
        model = ProductType
        fields = ['title', 'description', 'code']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Handmade Mugs'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Optional description',
                'rows': 3
            }),
            'code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., HDM (will be uppercase)',
                'maxlength': '10'
            }),
        }


class ProductForm(forms.ModelForm):
    """Form for creating and editing Products."""
    
    class Meta:
        model = Product
        fields = [
            'product_type', 'title', 'description',
            'initial_quantity', 'quantity_sold', 'is_unique',
            'length_in', 'width_in', 'height_in', 'weight_oz',
            'status', 'date_listed', 'date_sold_out'
        ]
        widgets = {
            'product_type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Product title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Optional product description',
                'rows': 3
            }),
            'initial_quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'min': '0'
            }),
            'quantity_sold': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'min': '0'
            }),
            'is_unique': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'length_in': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'min': '0',
                'placeholder': 'inches'
            }),
            'width_in': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'min': '0',
                'placeholder': 'inches'
            }),
            'height_in': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'min': '0',
                'placeholder': 'inches'
            }),
            'weight_oz': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'min': '0',
                'placeholder': 'ounces'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
            'date_listed': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'date_sold_out': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }


class ProductImageForm(forms.ModelForm):
    """Form for uploading product images."""
    
    class Meta:
        model = ProductImage
        fields = ['image', 'sort_order']
        widgets = {
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
            'sort_order': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'min': '0'
            }),
        }


# Inline formset for ProductImages when editing a Product
ProductImageFormSet = inlineformset_factory(
    Product,
    ProductImage,
    form=ProductImageForm,
    extra=1,
    can_delete=True
)
