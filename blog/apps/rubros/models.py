from django.db import models

# Create your models here.

class Rubros(models.Model):
    nombre = models.CharField(max_length=30) 

    def __str__(self):
        return self.nombre