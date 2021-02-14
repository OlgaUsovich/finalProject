from django.conf.urls import url
from django.urls import path, include
from django.views.generic import ListView, DetailView

from products.models import Product
from products.views import product_list

app_name = 'products'
urlpatterns = [
    #path('', ListView.as_view(model=Product, template_name='products/list.html'), name='list'),


    path('', product_list, name='list'),
    path('<int:pk>/', DetailView.as_view(model=Product, template_name='products/detail.html'), name='detail'),
    # path('<int:hello>/2/',
    #      DetailView.as_view(pk_url_kwarg='hello', model=Product, template_name='products/detail.html'), name='detail2'),
    path(r'^(P<category_slug>[-\w]+)/$', product_list, name='product_list_by_category'),



]
