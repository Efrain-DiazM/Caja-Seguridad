from django.db import models

# Create your models here.

class logins(models.Model):
    nombreLogin = models.CharField(max_length=15)
    email = models.EmailField(blank=False)
    usuario = models.CharField(max_length=15)
    contraseña = models.CharField(max_length=16)
    url = models.URLField(null=False)
    nota = models.CharField(max_length=255)

class identificacion(models.Model):
    nombreIdentificacion = models.CharField(max_length=15)
    numero = models.IntegerField(max_length=10)
    nombreCompleto = models.CharField(max_length=50)
    fechaNacimiento = models.DateField()
    fechaExpedicion = models.DateField()
    fechaVencimiento = models.DateField()
    nota = models.CharField(max_length=255)


