from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from authentication.views import CreateUserView, view_profile, profile_edit, change_password

app_name = 'authentication'
urlpatterns = [
    path('reg/', CreateUserView.as_view(), name='registration'),
    path('login/', LoginView.as_view(template_name='login.html', success_url='{% url "authentication:profile" %}',
                                     redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('profile/', view_profile, name='profile'),
    path('profile/<int:id>/edit/', profile_edit, name='edit_profile'),
    path('profile/change_password/', change_password, name='change_password')
]
