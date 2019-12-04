from django.db import models


class Factura(models.Model):
    idFactura=models.CharField(max_length=50)
    idUsuario=models.CharField(max_length=50)
    idProducto = models.CharField(max_length=50)
    cantidad = models.CharField(max_length=50)
