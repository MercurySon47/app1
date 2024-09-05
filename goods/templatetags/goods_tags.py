
# from urllib.parse import urlencode

from django import template
from django.utils.http import urlencode

from goods.models import Categories

register = template.Library() #Создаем регестратор Шаблонных тегов

# Декоратор Регестрируем Шаблонный тег.
@register.simple_tag() 
def tag_categories():
    return Categories.objects.all() # Получаем все значения из таблицы базы данных

# Декоратор Регестрируем Шаблонный тег с возможностью получения всех переменных из Контроллера Views.py
@register.simple_tag(takes_context=True) 
def change_params(context, **kwargs): # параметр **kwargs - получает не только значение но и название переменной. 
    query = context['request'].GET.dict() # из переменной context получаем значение по ключу request получаем данные в виде словоря.
    query.update(kwargs)
    return urlencode(query) # Формируем из словоря готовую ссылку