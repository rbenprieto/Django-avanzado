from django.urls import path
from .views import createAutor

urlpatterns = [
    path('crear-autor/', createAutor, name='autor-create')
]