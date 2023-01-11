from django.urls import path, re_path
from .views import (
    createAutor,
    # listarAutor,
    editarAutor,
    deleteAutor
)
from apps.libro.views import (
    ListAutoresView
)

urlpatterns = [
    path('crear-autor/', createAutor, name='autor-create'),
    path('listar-autor/', ListAutoresView.as_view(), name='autor-list'),
    path('update-autor/<str:pk>/', editarAutor, name='autor-editar'),
    path('delete-autor/<str:pk>/', deleteAutor, name='autor-eliminar'),
]