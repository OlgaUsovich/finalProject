from django.conf.urls import url
from django.urls import path

from cart import views

app_name = 'cart'
# urlpatterns = [
#     path('add/<int:product>/', add_to_cart, name='add')
# ]

urlpatterns = [
    url(r'^$', views.cart_detail, name='cart_detail'),
    url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
]