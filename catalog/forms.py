from django import forms
from django.core.exceptions import ValidationError
from .models import Product


class ProductForm(forms.ModelForm):
    # Список запрещенных слов
    FORBIDDEN_WORDS = [
        'казино', 'криптовалюта', 'крипта', 'биржа',
        'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
    ]

    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'purchase_price', 'image']

    def clean_name(self):
        """Валидация названия продукта на запрещенные слова"""
        name = self.cleaned_data.get('name', '')
        for word in self.FORBIDDEN_WORDS:
            if word.lower() in name.lower():
                raise ValidationError(f'Название не может содержать запрещенное слово: "{word}"')
        return name

    def clean_description(self):
        """Валидация описания продукта на запрещенные слова"""
        description = self.cleaned_data.get('description', '')
        for word in self.FORBIDDEN_WORDS:
            if word.lower() in description.lower():
                raise ValidationError(f'Описание не может содержать запрещенное слово: "{word}"')
        return description

    def clean_purchase_price(self):
        """Валидация цены продукта - не может быть отрицательной"""
        price = self.cleaned_data.get('purchase_price', 0)
        if price < 0:
            raise ValidationError('Цена не может быть отрицательной')
        return price

    def __init__(self, *args, **kwargs):
        """Стилизация формы"""
        super(ProductForm, self).__init__(*args, **kwargs)

        # Стилизация всех текстовых полей
        text_fields = ['name', 'description']
        for field in text_fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': f'Введите {self.fields[field].label.lower()}'
            })

        # Стилизация числового поля
        self.fields['purchase_price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену',
            'min': '0',
            'step': '0.01'
        })

        # Стилизация выпадающего списка
        self.fields['category'].widget.attrs.update({
            'class': 'form-control'
        })

        # Стилизация поля изображения
        self.fields['image'].widget.attrs.update({
            'class': 'form-control'
        })