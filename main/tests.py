from django.urls import reverse
from datetime import datetime

from django.test import TestCase
from rest_framework.test import APITestCase

from main.models import Form


# Create your tests here.
# Тестирование POST-запроса
class GetFormNameViewTest(TestCase):
    def test_post_request_with_matching_data(self):
        # Создаем тестовую форму в базе данных
        Form.objects.create(
            name_form='Тестовая форма',
            phone_field='+71234567890',
            email_field='test@example.com',
            text_field='Тестовый текст',
            data_field=datetime.now().strftime('%d.%m.%Y')
        )

        # Отправляем POST-запрос с данными
        response = self.client.post(
            reverse('main:get_form'),  # Замените 'get_form_name' на имя вашего URL-шаблона
            data={
                'phone_field': '+71234567890',
                'email_field': 'test@example.com',
                'text_field': 'Тестовый текст',
                'data_field': datetime.now().strftime('%d.%m.%Y')
            }
        )

        # Проверяем, что запрос вернул код 200 и содержит ожидаемый ответ
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'form_name': 'Тестовая форма'})

    def test_post_request_with_no_matching_data(self):
        # Отправляем POST-запрос с данными, которые не соответствуют форме в базе данных
        response = self.client.post(
            reverse('main:get_form'),  # Замените 'get_form_name' на имя вашего URL-шаблона
            data={
                'phone_field': '+71234567890',
                'email_field': 'test@example.com',
                'text_field': 'Тестовый текст',
                'data_field': datetime.now().strftime('%d.%m.%Y')
            }
        )

        # Проверяем, что запрос вернул код 200 и содержит ожидаемый ответ
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
                '1': 'Нет совпадений',
                '2': 'Указаны данные в разных формах',
                '3': 'Данные разных форм, не пересекаются',
                '4': 'Уменьшите количесвто данных, например оставьте только номер телефона',
                                 })
