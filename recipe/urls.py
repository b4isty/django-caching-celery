from django.urls import path

from .views import home
app_name = "recipe"
urlpatterns = [
    path("", home, name="home")
]
