# catalog/management/commands/create_moderator_group.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product

class Command(BaseCommand):
    help = 'Создает группу "Модератор продуктов" и назначает ей права'

    def handle(self, *args, **options):
        group_name = "Модератор продуктов"
        group, created = Group.objects.get_or_create(name=group_name)

        if created:
            self.stdout.write(f'✅ Группа "{group_name}" создана.')

            # Получаем контент-тип модели Product
            content_type = ContentType.objects.get_for_model(Product)

            # Назначаем права
            # 1. Разрешение на отмену публикации (кастомное)
            perm_unpublish, _ = Permission.objects.get_or_create(
                codename='can_unpublish_product',
                name='Может отменять публикацию продукта',
                content_type=content_type
            )
            group.permissions.add(perm_unpublish)

            # 2. Разрешение на удаление любого продукта (стандартное)
            perm_delete, _ = Permission.objects.get_or_create(
                codename='delete_product',
                name='Can delete product',
                content_type=content_type
            )
            group.permissions.add(perm_delete)

            self.stdout.write('✅ Права назначены.')
        else:
            self.stdout.write(f'ℹ️ Группа "{group_name}" уже существует.')

        self.stdout.write('🎉 Готово!')