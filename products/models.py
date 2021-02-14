from django.db import models


# Create your models here.
from django.urls import reverse

from authentication.models import User


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование товара')
    description = models.CharField(max_length=255, verbose_name='Описание')
    price = models.DecimalField('Цена', max_digits=6, decimal_places=2)
    size = models.ForeignKey('Size', on_delete=models.DO_NOTHING)
    stock = models.PositiveIntegerField("Количество на складе", default=1)
    available = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Товары'

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Фото товара', upload_to='products/')

    class Meta:
        verbose_name = 'Фото товаров'

    def __str__(self):
        return str(self.product) + self.image.url


class Size(models.Model):
    value = models.CharField("Значение", max_length=255)
    units = models.ForeignKey('Units', on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Размеры товаров'

    def __str__(self):
        return self.value + ' ' + str(self.units)


class Units(models.Model):
    value = models.CharField("Значение", max_length=255)

    class Meta:
        verbose_name = 'Единицы измерения размеров'

    def __str__(self):
        return self.value


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:product_list_by_category',
                       args=[self.slug])


class BasketItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_count = models.PositiveIntegerField("Количество")
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)


# class Order(models.Model):
#
#     statuses = ['Создан', 'В обработке', 'Ожидает доставку', 'Доставлен', 'Отменен']
#     payment_methods = ['Наличные', 'Карта']
#
#     number = models.CharField("Номер заказа")
#     # user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Пользователь')
#     status = models.CharField(choices=enumerate(statuses), verbose_name='Статус заказа')
#     basket_item = models.ForeignKey(BasketItem, on_delete=models.DO_NOTHING, verbose_name='Товар')
#     order_price = models.PositiveIntegerField("Общая сумма заказа")
#     delivery_address = models.CharField("Адрес доставки")
#     contacts = models.CharField("Контакты")
#     payment_method = models.CharField(choices=enumerate(payment_methods), verbose_name='Способ оплаты')

