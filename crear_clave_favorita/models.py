from django.db import models

# Create your models here.

class claveFavorita(models.Model):
    nombreClave = models.CharField(max_length=10)
    clave = models.CharField(max_length=16)
    confirmarClave = models.CharField(max_length=16)
    pista = models.CharField(max_length=10)