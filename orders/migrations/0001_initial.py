# Generated by Django 3.1.5 on 2021-02-13 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0005_product_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('phone', models.CharField(max_length=50, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='Адрес электронной почты')),
                ('address', models.CharField(max_length=250, verbose_name='Адрес')),
                ('postal_code', models.CharField(blank=True, max_length=20, null=True, verbose_name='Почтовый индекс')),
                ('city', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('paid', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_items', to='products.product')),
            ],
        ),
    ]