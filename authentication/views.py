from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView
from django.core.mail import send_mail
from django.conf import settings

from authentication.forms import RegistrationForm, ProfileEdit, ChangePasswordForm
from authentication.models import User


class CreateUserView(CreateView):
    model = User
    template_name = 'authentication/registration.html'
    form_class = RegistrationForm

    def get_success_url(self):
        url = reverse('authentication:email', kwargs={'pk': self.object.id})
        return url


@login_required
def view_profile(request):
    user_info = User.objects.get(username=request.user.username)
    return render(request, 'authentication/profile.html', {'user_info': user_info})


@login_required
def profile_edit(request, id):
    user_info = get_object_or_404(User, pk=id)
    if request.method == "POST":
        form = ProfileEdit(request.POST, instance=user_info)
        if form.is_valid():
            user_info = form.save(commit=False)
            user_info.save()
            return redirect('authentication:profile')
    else:
        form = ProfileEdit(instance=user_info)
    return render(request, 'authentication/edit_profile.html', {'form': form, 'user_info': user_info})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        passwords = request.POST
        user = request.user
        old_password = passwords['old_password']
        new_password1 = passwords['new_password1']
        new_password2 = passwords['new_password2']
        if check_password(old_password, user.password):
            if new_password1 == new_password2:
                user.set_password(new_password1)
                user.save()
                update_session_auth_hash(request, user)
                return redirect('authentication:profile')
            else:
                msg = "Повторенный пароль не соответствует исходному."
                form.add_error('new_password2', msg)
                context = {'form': form}
                return render(request, 'authentication/change_password.html', context)
        else:
            msg = "Введен неверный пароль."
            form.add_error('old_password', msg)
            if not new_password1 == new_password2:
                msg2 = "Повторенный пароль не соответствует исходному."
                form.add_error('new_password2', msg2)
                context = {'form': form}
                return render(request, 'authentication/change_password.html', context)
            context = {'form': form}
            return render(request, 'authentication/change_password.html', context)
    form = ChangePasswordForm()
    context = {'form': form}
    return render(request, 'authentication/change_password.html', context)


def email(request, pk):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [User.objects.filter(id=pk).first().email]
    send_mail(subject, message, email_from, recipient_list)
    return redirect('products:list')
