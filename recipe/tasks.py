from celery import shared_task
from celery_caching_django.celery import app as celery_app
from .models import Recipe


@celery_app.task
# @shared_task(bind=True)
def print_recipe():
    print("&&&&&&&&")
    print(Recipe.objects.first())

