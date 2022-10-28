from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import temporada
from .rabbit import share_temporada

@receiver(post_save, sender=temporada)
def brodcast_temporada(sender, instance, created, **args):
    tipo = 'temporada.update'
    if created:
        tipo = 'temporada.new'
    share_temporada(instance, tipo)
