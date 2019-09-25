from django.db import models
from apps.rubros.models import Rubros

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to = 'productos', null = True) #on_delete cuando se borre la relacion se borran todos los productos relacionados
    rubro = models.ForeignKey(Rubros, on_delete = models.CASCADE, related_name = "productosXrubro") #agregamos como clave foranea al modelo rubros , related_name hace que se llame desde rubro a sus productos

    def __str__(self):
        return self.nombre