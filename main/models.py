from datetime import datetime

from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
NULLABLE = {
    'null': True,
    'blank': True
}


class Form(models.Model):
    """Модель для форм"""
    name_form = models.CharField(max_length=70, verbose_name='Название (имя) формы')  # Название формы

    phone_regex = RegexValidator(regex=r'^\+7\d{11}$', message="Номер телефона в формате +7xxxxxxxxxx")  # Валидатор телефона, работает на создание
    phone_field = models.CharField(validators=[phone_regex], max_length=12, verbose_name='Номер телефона')  # поле номера телефона

    email_field = models.EmailField(max_length=50, verbose_name='Почта', help_text='Поле для почты')  # поле для почты, проевяется автоматически

    text_field = models.TextField(max_length=250, verbose_name='Какой то текст', **NULLABLE)  # поле текста

    data_field = models.DateField(auto_now_add=True, verbose_name='Дата, видимо дата создания')  # поле тады, сохраняется дата сохдания

    def save(self, *args, **kwargs):
        # Переопределяем метод save для сохранения даты в нужном формате
        if not self.data_field:
            self.data_field = datetime.now().strftime('%Y-%m-%d')  # форат даты гггг-мм-дд
        super().save(*args, **kwargs)

    def __str__(self):
        # строковое отображение для отладки
        return (f'Название формы {self.name_form};'
                f'номер телефона {self.phone_field};'
                f'почта {self.email_field};'
                f'дата создания {self.data_field};')

    class Meta:
        verbose_name = 'Форма'
        verbose_name_plural = 'Формы'
