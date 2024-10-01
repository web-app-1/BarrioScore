from django.db import models
from django.contrib.auth.models import User

class Promotor(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Residencial(models.Model):
    nombre = models.CharField(max_length=255)
    promotor = models.ForeignKey(Promotor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Resena(models.Model):
    CALIFICACION_OPCIONES = [
        (1, '1 - Pobre'),
        (2, '2 - Regular'),
        (3, '3 - Bueno'),
        (4, '4 - Muy Bueno'),
        (5, '5 - Excelente'),
    ]
    residencial = models.ForeignKey(Residencial, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    calificacion = models.IntegerField(choices=CALIFICACION_OPCIONES)
    comentario = models.TextField()
    hashtags = models.CharField(max_length=255, help_text="Agrega hashtags separados por comas")  # Nuevo campo de Hashtags
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reseña de {self.usuario.username} para {self.residencial.nombre}'
