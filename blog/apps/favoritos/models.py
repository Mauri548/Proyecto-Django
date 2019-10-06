from django.db import models
from apps.productos.models import Producto
from django.conf import settings

class Favorito(models.Model):
    producto = models.ForeignKey(Producto, on_delete = models.CASCADE, related_name = 'favoritoxproducto')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

    class Meta:
        unique_together=('user','producto')

    def __str__(self):
        return '#{}: {}'.format(self.producto, self.user)
