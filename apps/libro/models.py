from django.db import models
from apps.libro.choices import paises_CHOICES

class Autor(models.Model):
    id = models.AutoField(primary_key=True, editable=False, verbose_name='Id')
    nombre = models.CharField(max_length=255, verbose_name='Nombre')
    apellidos = models.CharField(max_length=255, verbose_name='Apellidos')
    activo = models.BooleanField(default=True, verbose_name='Autor activo')
    nacionalidad = models.CharField(max_length=100, choices=paises_CHOICES, verbose_name='Nacionalidad')

    def __str__(self):
        return str(self.nombre)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre']


class Libro(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    titulo = models.CharField(max_length=255, verbose_name='Titulo')
    fecha_publicacion = models.DateField(verbose_name='Fecha de publicación')
    autor_id = models.ManyToManyField(Autor)
    fecha_creacion = models.DateField(auto_now=True)
    
    def __str__(self):
        return str(self.titulo)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']