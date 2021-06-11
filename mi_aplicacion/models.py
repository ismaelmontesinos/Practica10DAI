from django.db import models

# Create your models here.
from django.utils import timezone

class Libro(models.Model):
  titulo = models.CharField(max_length=200)
  autor  = models.CharField(max_length=100)
  publicacion = models.DateField()
  prestado = models.BooleanField(default=False)
  veces_prestado = models.IntegerField(default=0)

  def __str__(self):
    return self.titulo

class Prestamo(models.Model):
  libro   = models.ForeignKey(Libro, on_delete=models.CASCADE)
  fecha   = models.DateTimeField(default=timezone.now)
  usuario = models.CharField(max_length=100)
  direccion = models.CharField(max_length=200,default=None)


  def __str__(self):
    return self.libro
