from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path(r'^create/$', views.order_create, name='order_create'),
    path('order_history/', views.show_history, name='order_history'),
    path(r'^export/xls/$', views.export_orders_xls, name='export_orders_xls')
]
