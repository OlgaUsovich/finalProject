from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if request.user.id:
                order.user = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])

            cart.clear()
            return render(request, 'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})


@login_required
def show_history(request):
    user = request.user
    orders = Order.objects.filter(user=user)
    for order in orders:
        order.sum = 0
        order_items = order.items.all()
        for item in order_items:
            order.sum += item.quantity * item.price
    return render(request, 'orders/order/orders_history.html', locals())
