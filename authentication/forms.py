from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import check_password
from django.forms import ModelForm

from authentication.models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'address']


class ProfileEdit(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'address']


class ChangePasswordForm(forms.ModelForm):
    old_password = forms.CharField(max_length=70, widget=forms.PasswordInput, label='Старый пароль')
    new_password1 = forms.CharField(max_length=70, widget=forms.PasswordInput, label='Новый пароль')
    new_password2 = forms.CharField(max_length=70, widget=forms.PasswordInput, label='Повторите пароль')

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']



