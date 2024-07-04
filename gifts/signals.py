from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Birthday

@receiver(post_delete, sender=Birthday)
def delete_media_files(sender, instance, **kwargs):
    if instance.img:
        instance.img.delete(False)




