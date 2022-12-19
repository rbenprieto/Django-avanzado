from django.contrib import admin
from apps.libro.models import Autor, Libro

# Register your models here.
admin.site.register(Autor)
admin.site.register(Libro)
