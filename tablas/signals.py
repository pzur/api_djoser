from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Paseador

@receiver(post_save, sender=User)
def create_paseador(sender, instance, created, **kwargs):
    if created:
        Paseador.objects.create(usuario=instance)
@receiver(post_save, sender=User)
def save_paseador(sender, instance, **kwargs):
    instance.usuario.save()
    