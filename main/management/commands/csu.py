# Создаем супер юзера
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):

    def handle(self, *args, **options):
        User = get_user_model()
        # Данные супер юзера
        username = 'admin'
        email = 'admin@admin.ru'
        password = 'qwerty'

        try:
            # Проверка существования пользователя
            user = User.objects.get(username=username)
            self.stdout.write(self.style.SUCCESS(f"Суперюзер '{username}' уже существует."))
        except Exception as e:
            # Если супер юезра нет он будет создан
            user = User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"Суперюзер '{username}' успешно создан!"))


