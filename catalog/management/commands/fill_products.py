from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Fill database with test products and categories'

    def handle(self, *args, **options):
        # Удаляем старые данные
        Product.objects.all().delete()
        Category.objects.all().delete()
        
        self.stdout.write('Удалены старые данные...')
        
        # Создаем категории
        categories_data = [
            {'name': 'Электроника', 'description': 'Электронные устройства и гаджеты'},
            {'name': 'Книги', 'description': 'Книги и учебная литература'},
            {'name': 'Одежда', 'description': 'Одежда и аксессуары'},
            {'name': 'Спорт', 'description': 'Спортивные товары'},
            {'name': 'Мебель', 'description': 'Мебель для дома и офиса'},
        ]
        
        categories = {}
        for cat_data in categories_data:
            category = Category.objects.create(**cat_data)
            categories[cat_data['name']] = category
            self.stdout.write(f'Создана категория: {category.name}')
        
        # Создаем продукты
        products_data = [
            {'name': 'Смартфон iPhone', 'description': 'Современный смартфон', 'purchase_price': 79999.99, 'category': categories['Электроника']},
            {'name': 'Ноутбук Dell', 'description': 'Мощный ноутбук для работы', 'purchase_price': 65999.99, 'category': categories['Электроника']},
            {'name': 'Наушники Sony', 'description': 'Беспроводные наушники', 'purchase_price': 12999.99, 'category': categories['Электроника']},
            {'name': 'Python для начинающих', 'description': 'Учебник по программированию', 'purchase_price': 1899.99, 'category': categories['Книги']},
            {'name': 'Джинсы', 'description': 'Классические джинсы', 'purchase_price': 3999.99, 'category': categories['Одежда']},
            {'name': 'Футбольный мяч', 'description': 'Профессиональный мяч', 'purchase_price': 2999.99, 'category': categories['Спорт']},
            {'name': 'Офисный стол', 'description': 'Деревянный стол', 'purchase_price': 15999.99, 'category': categories['Мебель']},
        ]
        
        for product_data in products_data:
            product = Product.objects.create(**product_data)
            self.stdout.write(f'Создан продукт: {product.name} - {product.purchase_price} руб.')
        
        self.stdout.write(
            self.style.SUCCESS('База данных успешно заполнена тестовыми данными!')
        )
