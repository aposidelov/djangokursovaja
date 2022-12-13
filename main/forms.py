from .models import Restaurant
from django.forms import ModelForm, TextInput, Textarea, Select, NumberInput


class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = [
            'title',
            'type',
            'description',
            'website',
            'longitude',
            'latitude',
            'prices',
            'open_hours',
            'address',
            'phone'
        ]
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть назву'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть опис'
            }),
            'type': Select(attrs={
                'class': 'form-control',
                'choices': Restaurant.TYPE_CHOICES
            }),
            'website': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть веб-сторінку'
            }),
            'longitude': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть довготу'
            }),
            'latitude': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть ширину'
            }),
            'prices': Select(attrs={
                'class': 'form-control',
                'choices': Restaurant.PRICE_CHOICES
            }),
            'open_hours': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть час коли відкриті наприклад (10:00-21:00)'
            }),
            'address': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть адресу'
            }),
            'phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть телефон'
            }),

        }
