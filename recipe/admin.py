from django.contrib import admin
from recipe.models import Category, Recipe
# Register your models here.
admin.site.register([Category, Recipe])
