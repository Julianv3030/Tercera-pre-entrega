from django import forms
from .models import Instructores, Cursos, Alumnos

class instructoresForm(forms.ModelForm):
    class Meta:
        model = Instructores
        fields = ["nombre", "apellido", "dni"]

class cursosForm(forms.ModelForm):
    class Meta:
        model = Cursos
        fields = ["nombre", "nivel"]

class alumnosForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = ["nombre", "apellido", "dni", "telefono"]