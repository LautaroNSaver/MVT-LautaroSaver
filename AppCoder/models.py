from django.db import models


class Familiares(models.Model): 
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    fecha = models.CharField(max_length=40)
    edad = models.IntegerField() # Create your models here.


# Create your models here.
