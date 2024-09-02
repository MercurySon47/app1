# from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories


def index(request):

    # categories = Categories.objects.all() # Перенесли в шаблонные теги
    context = {
        "title": "Home - Главная",
        "content": "Магазин мебели HOME",
        # "categories": categories, # Перенесли в шаблонные теги
    }

    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "Home - О нас",
        "content": "О нас",
        "text_on_page": "Мы прекрасный магазин мебели, у нас качественный товар",
    }

    return render(request, "main/about.html", context)
