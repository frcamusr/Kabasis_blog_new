from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Reporte(models.Model):
    TIPOS_DE_REPORTE = (
        ('tecnico', 'Técnico'),
        ('contenido', 'Contenido'),
        ('seguridad', 'Seguridad'),
        ('sugerencia', 'Sugerencia'),
        ('consulta', 'Consulta'),
        ('feedback', 'Feedback General'),
    )
    ESTADOS = (
        ('nuevo', 'Nuevo'),
        ('revision', 'En Revisión'),
        ('resuelto', 'Resuelto'),
    )
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    tipo = models.CharField(max_length=50, choices=TIPOS_DE_REPORTE)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    estado = models.CharField(max_length=50, choices=ESTADOS, default='nuevo')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo