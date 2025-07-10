
from django.urls import path
from . import views

urlpatterns = [
    path('',views.listaTarefa, nome='lista-tarefa'),
]