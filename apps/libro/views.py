from django.shortcuts import render, redirect, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .forms import AutorForm

from .models import (
    Autor,
    Libro,
)

def home(request):
    return render(request,'index.html')


def createAutor(request):
    if request.method == 'POST':
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect('libro:autor-list')
    
    else:
        autor_form = AutorForm()
    return render(request, 'libro/crear_autor.html', {'autor_form': autor_form})


def listarAutor(request):
    autores = Autor.objects.filter(activo=True).order_by('id')
    return render(request, 'libro/listar_autor.html', {'autores': autores})


def editarAutor(request, pk):
    autor = Autor.objects.filter(id=pk).first()
    if not autor:
        return render(request, 'libro/crear_autor.html', {'error': 'No existe el autor enviado'}, status=404)
    if request.method == 'GET':
        autor_form = AutorForm(instance=autor)
    else:
        autor_form = AutorForm(request.POST, instance=autor)
        if autor_form.is_valid():
            autor_form.save()
            return redirect('libro:autor-list')
    return render(request, 'libro/crear_autor.html', {'autor_form': autor_form})


def deleteAutor(request, pk):
    autor = Autor.objects.filter(id=pk).first()
    if not autor:
        return render(request, 'libro/crear_autor.html', {'error': 'No existe el autor enviado'}, status=404)
    if request.method == 'POST':
        autor.activo = False
        autor.save()
        return redirect('libro:autor-list')
    return render(request, 'libro/eliminar_autor.html', {'autor': autor}, status=200)