from django.db import models

# Create your models here.


class Clase(models.Model):
    name = models.CharField(max_length=30)
    n_student = models.IntegerField(3)
    professor = models.CharField(max_length=50)
    schedule = models.DateTimeField()

    def __str__(self):
        return self.name
