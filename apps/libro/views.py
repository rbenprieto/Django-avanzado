from django.shortcuts import render, redirect, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .forms import AutorForm
from django.views import generic

from .models import (
    Autor,
    Libro,
)

class InicioView(generic.TemplateView):
    template_name = 'index.html'

class ListAutoresView(generic.ListView):
    model = Autor
    template_name = 'libro/listar_autor.html'
    context_object_name = 'autores'
    queryset = Autor.objects.filter(activo=True).order_by('id')



def createAutor(request):
    if request.method == 'POST':
        # CREACIÓN MEDIANTE FORM
        # print(request.POST)
        # autor_form = AutorForm(request.POST)
        # if autor_form.is_valid():
        #     autor_form.save()
        #     return redirect('libro:autor-list')

        # CREACIÓN OBTENIENDO LA DATA DEL REQUEST
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        nacionalidad = request.POST.get('nacionalidad')
        Autor.objects.create(
            nombre=nombre,
            apellidos=apellidos,
            nacionalidad=nacionalidad
        )
        return redirect('libro:autor-list')

    
    # else:
    #     autor_form = AutorForm()
    return render(request, 'libro/crear_autor.html')

# def home(request):
#     return render(request,'index.html')

# def listarAutor(request):
#     autores = Autor.objects.filter(activo=True).order_by('id')
#     return render(request, 'libro/listar_autor.html', {'autores': autores})


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