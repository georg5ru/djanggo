from django.views.generic import ListView, DetailView, TemplateView
from .models import Product

# CBV — классы представлений

class HomeView(ListView):
    """Главная страница со списком товаров"""
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    """Страница с подробной информацией о товаре"""
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ContactsView(TemplateView):
    """Страница контактов"""
    template_name = 'catalog/contacts.html'