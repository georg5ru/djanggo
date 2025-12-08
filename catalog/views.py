# catalog/views.py
from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def home(request):
    """Главная страница со списком товаров"""
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/home.html', context)

def product_detail(request, pk):
    """Страница с подробной информацией о товаре"""
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'catalog/product_detail.html', context)

def contacts(request):
    """Страница контактов"""
    return render(request, 'catalog/contacts.html')