# from re import search # Пример простого поиска
# from django.db.models import Q # Пример простого поиска
from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    SearchHeadline
)
from goods.models import Products


# Функция поиска
def q_search(query):
    if (
        query.isdigit() and len(query) <= 5
    ):  # Если посикровый запрос int ищем по id сотоящий до 5 знаков
        return Products.objects.filter(id=int(query))  # возвращаем Товар с выбранным id

    vector = SearchVector("name", "description")
    query = SearchQuery(query)

    result = (
        Products.objects.annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)
        .order_by("-rank")
    )
    result = result.annotate(
        headline=SearchHeadline(
            "name",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel="</span>",
        )
    )

    result = result.annotate(
        bodyline=SearchHeadline(
            "description",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel="</span>",
        )
    )

    return result

    # Пример простого поиска
    # return Products.objects.filter(description__search=query)
    # keywords = [word for word in query.split() if len(word) > 2]
    # q_objects = Q() # создаем переменную назначаем ей тип Q
    # for token in keywords:
    #     q_objects |= Q(description__icontains=token) # поиск по описанию добовляем Q обьект в список
    #     q_objects |= Q(name__icontains=token) # поиск по названию добовляем Q обьект в список
    # return Products.objects.filter(q_objects)
