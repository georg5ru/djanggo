from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.http import HttpResponseForbidden


# FBV - старые функции

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


from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Product, Category
from .forms import ProductForm


# CBV для продуктов
class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'price']
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        # Привязываем текущего пользователя как владельца
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'price', 'is_published']
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()

        # Проверяем: владелец ИЛИ модератор?
        if product.owner != request.user and not request.user.groups.filter(name="Модератор продуктов").exists():
            return HttpResponseForbidden("Вы не можете редактировать этот продукт.")

        return super().dispatch(request, *args, **kwargs)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()

        # Владелец ИЛИ модератор может удалять
        if product.owner != request.user and not request.user.groups.filter(name="Модератор продуктов").exists():
            return HttpResponseForbidden("Вы не можете удалить этот продукт.")

        return super().dispatch(request, *args, **kwargs)
