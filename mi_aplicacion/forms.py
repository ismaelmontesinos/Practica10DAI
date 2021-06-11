from django import forms

from .models import Libro, Prestamo

class FormLibro(forms.ModelForm):

    class Meta:
        model = Libro
        fields = ('titulo', 'autor','publicacion')

class FormPrestamo(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ('usuario','direccion')
