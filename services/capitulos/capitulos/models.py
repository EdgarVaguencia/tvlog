from django.db import models

class temporada(models.Model):
    nombre = models.CharField(max_length=100)
    serie_id = models.IntegerField(blank=False, null=False, default=0)
    serie = models.CharField(max_length=100, default='')

    def __str__(self):
        return u'{} - {}'.format(self.temporada, self.serie)

class capitulo(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_lanzamiento = models.DateTimeField()
    temporada = models.ForeignKey(temporada, related_name='capitulos', on_delete=models.PROTECT)
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(auto_now=True)
    eliminado = models.BooleanField(default=False)
    fecha_eliminado = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return u'{} / {}'.format(self.nombre, self.temporada)
