from django.shortcuts import render

# Create your views here.
from django.db.models import Count
from .models import Product, Category
def home(request):
    products = Product.objects.filter(
        is_available=True
    ).order_by('price')

    categories = Category.objects.annotate(
        product_count=Count('products')
    ).filter(product_count__gt=0)

    return render(request, 'home.html', {
        'products': products,
        'categories': categories
    })
def sale_products(request):
    products = Product.objects.filter(
        is_sale=True,
        is_available=True
    )
    return render(request, 'sale.html', {'products': products})

