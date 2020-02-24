from django import forms
from home.models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('name', 'email','body','picture')
