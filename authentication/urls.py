from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from authentication.views import CreateUserView, view_profile, profile_edit, change_password, email, show_all_orders, \
    order_edit

app_name = 'authentication'
urlpatterns = [
    path('reg/', CreateUserView.as_view(), name='registration'),
    path('login/',
         LoginView.as_view(template_name='authentication/login.html', success_url='{% url "authentication:profile" %}',
                           redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('profile/change_password/', change_password, name='change_password'),
    path('profile/<int:id>/edit/', profile_edit, name='edit_profile'),
    path('profile/', view_profile, name='profile'),
    path('email/<int:pk>/', email, name='email'),
    path('received_orders/', show_all_orders, name='received_orders'),
    path('edit_order/<int:pk>/', order_edit, name='order_edit'),

]
