from django.urls import path
from .views import home, sale_products

urlpatterns = [
    path('', home, name='home'),
    path('sale/', sale_products, name='sale'),
]
