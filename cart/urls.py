from django.urls import path

from cart.views import add_to_cart

app_name = 'cart'
urlpatterns = [
    path('add/<int:product>/', add_to_cart, name='add')
]