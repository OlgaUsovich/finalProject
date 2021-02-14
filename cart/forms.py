from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.CharField(label='Количество', initial=1, widget=forms.TextInput(attrs={'style': 'width: 25px'}))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

