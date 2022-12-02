from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.conf import settings
from .models import Category, Recipe
from recipe.tasks import print_recipe

# Create your views here.


# @cache_page(60 * 1)
def home(requests):
    recipes = cache.get("recipes", [], version=settings.CACHE_VERSION)
    print("**************** before delay")
    print_recipe.delay()
    # print_recipe.apply_async(countdown=10)
    print("************* after delay")
    if not recipes:
        recipes = Recipe.objects.all()
        cache.set("recipes", recipes, settings.CACHE_TTL, version=settings.CACHE_VERSION)
    contexts = {"recipes": recipes}
    return render(requests, "home.html", contexts)


