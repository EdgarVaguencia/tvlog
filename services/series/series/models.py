from django.db import models

class serie(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(auto_now=True)
    eliminado = models.BooleanField(default=False)
    fecha_eliminado = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return u'{}'.format(self.nombre)
