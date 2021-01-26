from django.db import models


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование товара')
    description = models.CharField(max_length=255, verbose_name='Описание')
    price = models.DecimalField('Цена', max_digits=6, decimal_places=2)
    size = models.ForeignKey('Size', on_delete=models.DO_NOTHING)

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
        return str(self.product)


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


class BasketItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_count = models.PositiveIntegerField("Количество")
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)


