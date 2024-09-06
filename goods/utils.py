from django.db.models import Q

from goods.models import Products

# Функция поиска
def q_search (query): 
    if query.isdigit() and len(query) <=5: # Если посикровый запрос int ищем по id сотоящий до 5 знаков
        return Products.objects.filter(id=int(query)) # возвращаем Товар с выбранным id  
    
    keywords = [word for word in query.split() if len(word) > 2]
    
    q_objects = Q() # создаем переменную назначаем ей тип Q 

    for token in keywords:
        q_objects |= Q(description__icontains=token) # поиск по описанию добовляем Q обьект в список
        q_objects |= Q(name__icontains=token) # поиск по названию добовляем Q обьект в список
    
    return Products.objects.filter(q_objects)

