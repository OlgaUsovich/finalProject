from django.conf.urls import url
from django.urls import path, include
from django.views.generic import ListView, DetailView

from cart.views import product_detail
from products.models import Product
from products.views import product_list, MySearch

app_name = 'products'
urlpatterns = [
    path('', product_list, name='list'),
    path('<int:id>/', product_detail, name='detail'),
    # url(r'^(P<category_slug>[-\w]+)/$', product_list, name='product_list_by_category'),
    path('<str:category_slug>', product_list, name='product_list_by_category'),
    # path('search/', MySearch.as_view(), name='search'),
    path('search/', MySearch.as_view(), name='search'),
]
