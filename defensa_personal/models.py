from django.db import models

class Cursos(models.Model):
    nombre = models.CharField(max_length=64)
    nivel = models.IntegerField()

class Alumnos(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    telefono = models.CharField(max_length=20, blank=True)
    fecha_nacimiento = models.DateField(null=True)

class Instructores(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    arte_marcial = models.CharField(max_length=128)


