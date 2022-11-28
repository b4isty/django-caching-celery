from django.shortcuts import render
from django.views.decorators.cache import cache_page

from .models import Category, Recipe

# Create your views here.

@cache_page(180)
def home(requests):
    recipe = Recipe.objects.all()
    contexts = {"recipes": recipe}
    return render(requests, "home.html", contexts)
