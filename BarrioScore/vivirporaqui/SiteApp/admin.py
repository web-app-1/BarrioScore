from django.contrib import admin
from .models import Promotor, Residencial, Resena

class ResenaAdmin(admin.ModelAdmin):
    list_display = ('residencial', 'usuario', 'calificacion', 'comentario', 'fecha_publicacion')  # Agregamos la fecha aquí

admin.site.register(Promotor)
admin.site.register(Residencial)
admin.site.register(Resena, ResenaAdmin)  # Registramos Resena con ResenaAdmin


