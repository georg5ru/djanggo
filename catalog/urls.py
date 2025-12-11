from django.urls import path
from . import views
from .views import (
    ProductListView, ProductCreateView,
    ProductUpdateView, ProductDeleteView
)

urlpatterns = [
    # Существующие URL
    path('', views.home, name='home'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('contacts/', views.contacts, name='contacts'),

    # Новые URL для CRUD операций
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('category/<str:category_name>/', views.products_by_category, name='products_by_category'),
]