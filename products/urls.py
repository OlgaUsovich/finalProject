from django.urls import path
from django.views.generic import ListView

from products.models import Product

app_name = 'products'
urlpatterns = [
    path('', ListView.as_view(model=Product, template_name='products/list.html'), name='list'),
]
