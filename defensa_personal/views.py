from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse


def bienvenida(request):
    bienvenido = "Hola querido usuario"
    pagina_html = HttpResponse(bienvenido)
    return pagina_html