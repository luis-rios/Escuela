from django.db import models

# Create your models here.
from Escuela.Clase.models import Clase


class Estudiante(models.Model):
    name = models.CharField(max_length=50)
    lastNAme = models.CharField(max_length=50)
    birth = models.DateField()
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE, related_name='estudiante')

    def __str__(self):
        return self.name
