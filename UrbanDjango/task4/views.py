from django.shortcuts import render
from django.views.generic import TemplateView


def platform(request):
    data = {"title": "Главная страница"}
    return render(request, "fourth_task/platform.html", data)


def games(request):
    data = {
        "title": "Игры",
        'games': ["Atomic Heart", "Cyberpunk 2077", "Pay Day 2"]}
    return render(request, "fourth_task/games.html", context=data)


def cart(request):
    data = {"title": "Корзина"}
    return render(request, "fourth_task/cart.html", data)
