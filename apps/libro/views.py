from django.shortcuts import render, redirect
from .forms import AutorForm
from .models import (
    Autor,
    Libro,
)

def home(request):
    return render(request,'index.html')


def createAutor(request):
    print('metodo:', request.method)
    if request.method == 'POST':
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect('index')
    
    else:
        autor_form = AutorForm()
    return render(request, 'libro/crear_autor.html', {'autor_form': autor_form})

def listarAutor(request):
    autores = Autor.objects.all()
    return render(request, 'libro/listar_autor.html', {'autores': autores})

def editarAutor(request):
    pass