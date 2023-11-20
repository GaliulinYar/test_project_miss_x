from datetime import datetime

from django.core.validators import validate_email
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from main.models import Form


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch') # Отключаем авторизацию
class GetFormNameView(View):
    def post(self, request, *args, **kwargs):

        # Получаем значения из POST-запроса
        phone_value = request.POST.get('phone_field')
        email_value = request.POST.get('email_field')
        text_value = request.POST.get('text_field')
        data_value = request.POST.get('data_field')

        # Инициализируем пустой словарь для фильтра
        form_data = {}

        # Проверяем, какие поля были переданы и добавляем их в фильтр
        if phone_value:
            if phone_value[:2] == '+7' and len(phone_value) == 12:
                form_data['phone_field'] = phone_value
            else:
                return JsonResponse({'phone_field': 'Телефон в формате +7хххххххххх'})

        if email_value:
            if '@' in email_value:
                form_data['email_field'] = email_value
            else:
                return JsonResponse({'email_field': 'Почта в формате xxx@xxx.xxx'})

        if text_value:
            form_data['text_field'] = text_value

        if data_value:
            try:
                datetime.strptime(data_value, '%d.%m.%Y')
                # Преобразовываем формат даты для поиска в базе данных
                formatted_data_value = datetime.strptime(data_value, '%d.%m.%Y').strftime('%Y-%m-%d')
                form_data['data_field'] = formatted_data_value
            except ValueError:
                return JsonResponse({'data_field': 'Формат даты дд.мм.гггг'})

        print(form_data)
        # Ищем совпадения в БД
        matching_forms = Form.objects.filter(**form_data)
        print(matching_forms)
        if matching_forms.exists():
            # Если есть совпадения, возвращаем список подходящих форм

            form_names = [form.name_form for form in matching_forms]
            if len(form_names) > 1:
                return JsonResponse({'form_names': form_names})
            else:
                return JsonResponse({'form_name': form_names[0]})
        else:
            return JsonResponse({
                '1': 'Нет совпадений',
                '2': 'Указаны данные в разных формах',
                '3': 'Данные разных форм, не пересекаются',
                '4': 'Уменьшите количесвто данных, например оставьте только номер телефона',
                                 })
