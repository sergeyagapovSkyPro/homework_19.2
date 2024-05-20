from django import forms

from catalog.models import Product, Version
from common.views import StyleFormMixin


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'created_at', 'updated_at', 'price', 'image')

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in words:
            if word in cleaned_data:
                raise forms.ValidationError('Ошибка в названии')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in words:
            if word in cleaned_data:
                raise forms.ValidationError('Ошибка в названии, у нас такого нет!')
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
