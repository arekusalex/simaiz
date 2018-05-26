from django.urls import path
from .views import inicio, direccionar
from .views import MultipleFormsDemoView

urlpatterns = [
    path('', inicio, name="inicio"),
    path('', direccionar, name="sim_lista"),
    path('nuevo/', MultipleFormsDemoView.as_view(), name="nuevo_sim"),
]