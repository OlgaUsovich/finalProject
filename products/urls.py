from django.conf.urls import url
from django.urls import path, include
from django.views.generic import ListView, DetailView

from cart.views import product_detail
from products.models import Product
from products.views import product_list

app_name = 'products'
urlpatterns = [
    #path('', ListView.as_view(model=Product, template_name='products/list.html'), name='list'),

# DetailView.as_view(model=Product, template_name='products/detail.html')
    path('', product_list, name='list'),
    path('<int:id>/', product_detail, name='detail'),
    # path('<int:hello>/2/',
    #      DetailView.as_view(pk_url_kwarg='hello', model=Product, template_name='products/detail.html'), name='detail2'),
    path(r'^(P<category_slug>[-\w]+)/$', product_list, name='product_list_by_category'),



]
