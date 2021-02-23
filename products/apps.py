from django.apps import AppConfig
from watson import search as watson


class ProductsConfig(AppConfig):
    name = 'products'

    def ready(self):
        products = self.get_model('Product')
        watson.register(products)
