from django.db import models

class serie(models.Model):
    id_origen = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return u'{}'.format(self.nombre)

class temporada(models.Model):
    nombre = models.CharField(max_length=100)
    serie = models.ForeignKey(serie, related_name='temporadas', on_delete=models.PROTECT)
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(auto_now=True)
    eliminado = models.BooleanField(default=False)
    fecha_eliminado = models.DateTimeField(blank=True, null=True)
    num_capitulos = models.IntegerField(default=0)

    def __str__(self):
        return u'{} - {}'.format(self.serie, self.nombre)

    def get_nombre_serie(self):
        return self.serie
