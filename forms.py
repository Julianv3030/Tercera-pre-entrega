from django import forms
from .models import instructores, cursos, Alumnos

class instructoresForm(forms.ModelForm):
    class Meta:
        model = instructores
        fields = ["nombre", "apellido", "dni", "telefono", "fecha de nacimiento"]

class cursosForm(forms.ModelForm):
    class Meta:
        model = cursos
        fields = ["nombre", "nivel"]

class alumnosForm(forms.ModelForm):
    class Meta:
        model = alumnos
        fields = ["nombre", "apellido", "dni", "telefono", "fecha de nacimiento"]