from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from main.views import GetFormNameView

app_name = 'main'  # Установка app_name для приложения

urlpatterns = [
    path('get_form/', GetFormNameView.as_view(), name='get_form'),  # патерн(урл) для пост запроса
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    ]
