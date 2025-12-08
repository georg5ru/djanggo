from django.contrib import admin
from django.urls import path, include  # ← Обязательно добавь include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')),  # ← Подключаем маршруты из приложения catalog
]