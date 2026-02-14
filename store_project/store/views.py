from django.db.models import Count
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Product, Category
from .forms import ProductCreateForm, ProductUpdateForm

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["products"] = Product.objects.filter(is_available=True)

        context["categories"] = Category.objects.annotate(
            product_count=Count("products")
        ).filter(product_count__gt=0)

        return context
class SaleProductsView(ListView):
    model = Product
    template_name = "sale.html"
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.filter(
            is_sale=True,
            is_available=True
        )
class CategoryProductsView(ListView):
    model = Product
    template_name = "category_products.html"
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.filter(
            category_id=self.kwargs["id"],
            is_available=True
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.get(id=self.kwargs["id"])
        return context
class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"
    pk_url_kwarg = "id"

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = "product_form.html"
    success_url = reverse_lazy("home")

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductUpdateForm
    template_name = "product_form.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("home")
class ProductDeleteView(DeleteView):
    model = Product
    pk_url_kwarg = "id"
    success_url = reverse_lazy("home")