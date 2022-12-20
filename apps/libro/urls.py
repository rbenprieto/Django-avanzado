from django.urls import path, re_path
from .views import (
    createAutor,
    listarAutor,
    editarAutor,
    deleteAutor
)

urlpatterns = [
    path('crear-autor/', createAutor, name='autor-create'),
    path('listar-autor/', listarAutor, name='autor-list'),
    path('update-autor/<str:pk>/', editarAutor, name='autor-editar'),
    path('delete-autor/<str:pk>/', deleteAutor, name='autor-eliminar'),
]