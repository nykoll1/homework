from .models import Product

def last_products(request):
    return {
        'last_products': Product.objects.order_by('-created_at')[:5]
    }