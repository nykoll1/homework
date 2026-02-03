from django.shortcuts import render, get_object_or_404

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

def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    products = Product.objects.filter(
        category=category,
        is_available=True
    )

    return render(request, 'category_products.html', {
        'category': category,
        'products': products
    })
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    return render(request, 'product_detail.html', {
        'product': product
    })
