from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.db.models import Count
from .models import Product, Category

from .forms import ProductCreateForm, ProductUpdateForm
def home(request):
    products = Product.objects.filter(is_available=True)

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

def category_products(request, id):
    category = get_object_or_404(Category, id=id)

    products = Product.objects.filter(
        category=category,
        is_available=True
    )

    return render(request, 'category_products.html', {
        'category': category,
        'products': products
    })
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)

    return render(request, 'product_detail.html', {
        'product': product
    })
#class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['is_available']


#class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('_all_',)


def product_create(request):
    form = ProductCreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'product_form.html', {'form': form})


def product_update(request, id):
    product = get_object_or_404(Product, id=id)
    form = ProductUpdateForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'product_form.html', {'form': form})


def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('home')