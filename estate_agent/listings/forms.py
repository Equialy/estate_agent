from django import forms
from .models import Listings


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listings
        fields = ['title', 'description', 'price', 'property_type', 'deal_type',
                  'address', 'rooms', 'area', 'status']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название объявления'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Описание недвижимости'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена'
            }),
            'property_type': forms.Select(attrs={
                'class': 'form-select'
            }),
            'deal_type': forms.Select(attrs={
                'class': 'form-select'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Полный адрес'
            }),
            'rooms': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество комнат'
            }),
            'area': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Площадь в м²'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Добавляем обязательные поля
        for field_name, field in self.fields.items():
            if field.required:
                field.widget.attrs['required'] = True
