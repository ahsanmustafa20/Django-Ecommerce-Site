from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['items','name', 'email', 'address', 'city', 'state', 'zip','total']