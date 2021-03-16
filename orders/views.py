from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.db.models import QuerySet
from django.shortcuts import render, redirect

from finalProject import settings
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
import xlwt
from django.http import HttpResponse


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
    user_info = request.user
    orders = Order.objects.filter(user=user_info)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    paginator = Paginator(orders, 5)
    pages = paginator.get_page(page_num)
    for order_ in orders:
        order_.sum = 0
        order_items = order_.items.all()
        for item in order_items:
            order_.sum += item.quantity * item.price
    return render(request, 'orders/order/orders_history.html', locals())


def export_orders_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="orders.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Orders')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Номер заказа', 'Имя', 'Фамилия', 'Email', 'Адрес', 'Дата создания']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    date_created = [i['created'].strftime('%d.%M.%Y') for i in Order.objects.values('created')]

    rows = Order.objects.all().values_list('id', 'first_name', 'last_name', 'email', 'address')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
        ws.write(row_num, len(row), date_created[row_num-1], font_style)

    wb.save(response)
    return response
