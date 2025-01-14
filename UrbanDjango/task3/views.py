from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class Platform(TemplateView):
    template_name = "third_task/platform.html"


class Games(TemplateView):
    template_name = "third_task/games.html"


class Cart(TemplateView):
    template_name = "third_task/cart.html"
