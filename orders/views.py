from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from finalProject import settings
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
            order_list = []
            for item in cart:
                order_list.append(
                    str(item['product']) + ' - ' + str(item['quantity']) + 'шт. Цена: ' + str(item['price']) + 'p.')
            subject = 'Заказ на Flechazo Lingerie'
            message = order.first_name + ' ' + order.last_name + ', Вы оформили заказ на Flechazo Lingerie!\n\nЗаказ №' + str(
                order.id) + '\n' + '\n'.join(
                order_list) + '\n\nСумма заказа: ' + str(
                order.get_total_cost()) + '\n\nВ ближайшее время с Вами свяжется наш менеджер. Спасибо за заказ!'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [order.email]
            send_mail(subject, message, email_from, recipient_list)
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
