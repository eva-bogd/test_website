from django import forms

from .models import Service


class ServiceForm(forms.ModelForm):
    """Форма создания услуги"""
    class Meta:
        model = Service
        fields = ('category', 'name', 'image', 'description', 'price')
