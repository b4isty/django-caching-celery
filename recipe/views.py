from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.conf import settings
from .models import Category, Recipe

# Create your views here.


# @cache_page(60 * 1)
def home(requests):
    recipes = cache.get("recipes", [], version=settings.CACHE_VERSION)
    if not recipes:
        recipes = Recipe.objects.all()
        cache.set("recipes", recipes, settings.CACHE_TTL, version=settings.CACHE_VERSION)
    contexts = {"recipes": recipes}
    return render(requests, "home.html", contexts)
