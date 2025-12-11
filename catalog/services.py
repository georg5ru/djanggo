from .models import Product

def get_products_by_category(category_name):
    """
    Возвращает список продуктов по указанной категории.
    """
    return Product.objects.filter(category=category_name, is_published=True)