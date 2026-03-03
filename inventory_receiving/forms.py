from django import forms
from django.forms import inlineformset_factory
from .models import ProductType, Product, ProductImage


class ProductTypeSelect(forms.Select):
    """Select widget that adds data attributes from the related ProductType to each <option>."""

    def create_option(self, name, value, label, selected, index, **kwargs):
        option = super().create_option(name, value, label, selected, index, **kwargs)
        if value:
            try:
                product_type = ProductType.objects.get(pk=int(str(value)))
                option['attrs']['data-code'] = product_type.code
                option['attrs']['data-next-sku-number'] = product_type.next_sku_number
            except (ProductType.DoesNotExist, ValueError):
                pass
        return option


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

    # Non-model field: pounds portion of weight
    weight_lb = forms.IntegerField(
        label='Weight (lbs)',
        min_value=0,
        required=False,
        initial=0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'type': 'number',
            'min': '0',
            'placeholder': 'pounds'
        })
    )

    class Meta:
        model = Product
        fields = [
            'product_type', 'title', 'description',
            'initial_quantity', 'quantity_sold', 'is_unique',
            'length_in', 'width_in', 'height_in', 'weight_oz',
            'status', 'date_listed', 'date_sold_out'
        ]
        widgets = {
            'product_type': ProductTypeSelect(attrs={
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
                'max': '15',
                'placeholder': 'oz (0-15)'
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # When editing an existing product, split stored total ounces into lbs + oz
        if self.instance.pk:
            total_oz = self.instance.weight_oz
            self.initial['weight_lb'] = total_oz // 16 # Floor division to get pounds
            self.initial['weight_oz'] = total_oz % 16 # Remainder after dividing by 16

    def clean_weight_oz(self):
        oz = self.cleaned_data.get('weight_oz') or 0
        if oz > 15:
            raise forms.ValidationError(
                "Ounces must be 0-15. Use the pounds field for full pounds."
            )
        return oz

    def clean(self):
        cleaned_data = super().clean()
        weight_lb = cleaned_data.get('weight_lb') or 0
        weight_oz = cleaned_data.get('weight_oz') or 0
        # Store combined total as ounces in the model field
        cleaned_data['weight_oz'] = weight_lb * 16 + weight_oz
        return cleaned_data


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
