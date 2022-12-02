import os
from celery import Celery
from django.conf import settings
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celery_caching_django.settings")
app = Celery(
    "celery_caching_django",
    # broker=settings.CELERY_BROKER_URL,
    # backend="rpc://",
    # include=["celery_caching_django.tasks", "recipe.tasks"]


)

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

# if __name__ == "__main__":
#     app.start()
