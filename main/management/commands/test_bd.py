# Создаем супер юзера
from django.core.management.base import BaseCommand

from main.models import Form


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Открываем БД'))

        for i in range(1, 6):  # Создаем 5 экземплаяров наших моделей(форм
            form_instance = Form(
                name_form=f'Форма {i}',
                phone_field=f'+7654321890{i}',
                email_field=f'test{i}@test.ru',
                text_field=f'Текст {i}',
            )
            form_instance.save()

            self.stdout.write(self.style.SUCCESS(f'Форма {i} загружена'))

        form_instance = Form(
            name_form=f'Форма 1-1',
            phone_field=f'+76543218901',
            email_field=f'test1@test.ru',
            text_field=f'Текст 1',
        )
        form_instance.save()

        self.stdout.write(self.style.SUCCESS(f'Дубль форма 1 загружена'))

        self.stdout.write(self.style.SUCCESS('Тестовая БД создана'))
