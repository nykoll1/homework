from django.urls import path
from .views import home, sale_products, category_products, product_detail
from .views import *
from . import views

urlpatterns = [
   path('product/<int:id>/', product_detail, name='product_detail'),
   path('product/add/', product_create, name='product_create'),
   path('product/update/<int:id>/', product_update, name='product_update'),
   path('product/delete/<int:id>/', product_delete, name='product_delete'),
   
   
   path('', home, name='home'),
   path('category/<int:id>/', category_products, name='category_products'),
]
