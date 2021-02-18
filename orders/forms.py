from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    user = forms.IntegerField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'email', 'address', 'postal_code', 'city']
