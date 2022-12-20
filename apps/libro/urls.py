from django.urls import path, re_path
from .views import (
    createAutor,
    listarAutor
)

urlpatterns = [
    path('crear-autor/', createAutor, name='autor-create'),
    path('listar-autor/', listarAutor, name='autor-list'),
    path('listar-autor/<str:pk>/', listarAutor, name='autor-list'),
    re_path('listar-autor/', listarAutor, name='autor-list'),
]