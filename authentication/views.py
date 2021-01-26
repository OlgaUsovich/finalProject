from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.views.generic import CreateView

from authentication.forms import RegistrationForm
from authentication.models import User


class CreateUserView(CreateView):
    model = User
    template_name = 'registration.html'
    form_class = RegistrationForm
    success_url = '/'

