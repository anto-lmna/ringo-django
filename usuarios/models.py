# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre_perfil = models.CharField(max_length=100)
    edad = models.IntegerField()
    deporte = models.CharField(
        max_length=50, choices=[("boxeo", "Boxeo"), ("kickboxing", "Kickboxing")]
    )
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre_perfil
