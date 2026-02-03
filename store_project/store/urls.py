from django.urls import path
from .views import home, sale_products, category_products, product_detail

urlpatterns = [
    path('', home, name='home'),
    path('sale/', sale_products, name='sale'),
    path('category/<int:category_id>/', category_products, name='category_products'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
]
