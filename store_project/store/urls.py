from django.urls import path
from .views import (
    HomeView,
    SaleProductsView,
    CategoryProductsView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView
)
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('sale/', SaleProductsView.as_view(), name='sale_products'),
    path('category/<int:id>/', CategoryProductsView.as_view(), name='category_products'),

    path('product/<int:id>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:id>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:id>/', ProductDeleteView.as_view(), name='product_delete'),
]