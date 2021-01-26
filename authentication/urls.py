from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from authentication.views import CreateUserView

app_name = 'authentication'
urlpatterns = [
    path('reg/', CreateUserView.as_view(), name='registration'),
    path('login/', LoginView.as_view(template_name='login.html', success_url='http://127.0.0.1:8000/', redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]