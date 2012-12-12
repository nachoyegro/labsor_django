from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    mail = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=16)
