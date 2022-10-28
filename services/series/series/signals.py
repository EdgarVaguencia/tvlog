from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import serie
from .rabbit import share_serie

@receiver(post_save, sender=serie)
def brodcast_serie(sender, instance, created, **args):
    tipo = 'serie.update'
    if created:
        tipo = 'serie.new'
    share_serie(instance, tipo)
