from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def add_to_cart(request,  product):
    if 'cart' not in request.session:
        request.session['cart'] = {}
    request.session['cart'][product] = request.GET.get('quantity', 1)
    return HttpResponse("Товар добавлен")

