from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from authentication.models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'phone', 'address']
