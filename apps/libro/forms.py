from django import forms
from .models import Autor, Libro

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

