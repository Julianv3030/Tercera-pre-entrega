from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from .forms import instructoresForm, cursosForm, alumnosForm  

def bienvenida(request):
    bienvenido = "Hola querido usuario"
    pagina_html = HttpResponse(bienvenido)
    return pagina_html

def ingresar(request):
    instructores_form = instructoresForm()
    cursos_form = cursosForm()
    alumnos_form = alumnosForm()

    if request.method == 'POST':
        instructores_form = instructoresForm(request.POST)
        cursos_form = cursosForm(request.POST)
        alumnos_form = alumnosForm(request.POST)

        if instructores_form.is_valid():
            instructores_form.save()

        if cursos_form.is_valid():
            cursos_form.save()

        if alumnos_form.is_valid():
            alumnos_form.save()

    return render(request, 'ingresar.html', {
        'instructores_form': instructores_form,
        'cursos_form': cursos_form,
        'alumnos_form': alumnos_form,
    })

def buscar(request):
    resultados = None

    if request.method == 'POST':
        busqueda = request.POST.get('busqueda', '')

        resultados_instructores = instructores.objects.filter(nombre__icontains=busqueda)
        resultados_cursos = cursos.objects.filter(nombre__icontains=busqueda)
        resultados_alumnos = alumnos.objects.filter(nombre__icontains=busqueda)

        resultados = {
            'instructores': resultados_instructores,
            'cursos': resultados_cursos,
            'alumnos': resultados_alumnos,
        }

    return render(request, 'buscar.html', {'resultados': resultados})