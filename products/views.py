from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

# Create your views here.
from cart.forms import CartAddProductForm
from products.models import Category, Product


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    paginator = Paginator(products, 12)
    page = paginator.get_page(page_num)
    cart_product_form = CartAddProductForm()

    content = {'category': category,
               'categories': categories,
               'page_object': page,
               'cart_product_form': cart_product_form}
    return render(request, 'products/list.html', content)
