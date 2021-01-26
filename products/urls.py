from django.urls import path
from django.views.generic import ListView, DetailView

from products.models import Product

app_name = 'products'
urlpatterns = [
    path('', ListView.as_view(model=Product, template_name='products/list.html'), name='list'),
    path('<int:pk>/', DetailView.as_view(model=Product, template_name='products/detail.html'), name='detail'),
    path('<int:hello>/2/',
         DetailView.as_view(pk_url_kwarg='hello', model=Product, template_name='products/detail.html'), name='detail2'),
]
