from django.urls import path
from django.config.urls import url
from .views
from .views import inicio

urlpatterns = [
    path('', inicio, name="inicio"),
]