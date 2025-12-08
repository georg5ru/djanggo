from django.shortcuts import render

def home(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    return render(request, 'catalog/contacts.html')

# catalog/views.py
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <h1>Добро пожаловать в мой магазин!</h1>
    <p>Это главная страница проекта.</p>
    <ul>
        <li><a href="/admin/">Админка</a></li>
        <li><a href="/admin/catalog/category/">Категории</a></li>
        <li><a href="/admin/catalog/product/">Продукты</a></li>
    </ul>
    """)

