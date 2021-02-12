from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

# Create your views here.
from products.models import Category, Product


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    paginator = Paginator(products, 10)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)

    content = {'category': category,
               'categories': categories,
               'object_list': products,
               'page': page}
    return render(request, 'products/list.html', content)
