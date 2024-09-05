from django.db.models import Q

from goods.models import Products

# Функция поиска
def q_search (query): 
    if query.isdigit() and len(query) <=5: # Если посикровый запрос int ищем по id сотоящий до 5 знаков
        return Products.objects.filter(id=int(query)) # возвращаем Товар с выбранным id  