from django.db import models

# Create your models here.

class Familia(models.Model):
    nombre = models.CharField(max_lenght = 40)
    apellido = models.CharField(max_lenght = 40)
    edad = models.IntegerField()
    nacimiento = models.DateField()
    email = models.EmailField()