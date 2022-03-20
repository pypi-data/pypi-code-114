from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from simpel.simpel_payments.models import Payment


@receiver(post_save, sender=Payment)
def after_save_receipt(sender, instance, **kwargs):
    if instance.reference is not None:
        instance.reference.save()


@receiver(post_delete, sender=Payment)
def after_delete_receipt(sender, instance, **kwargs):
    if instance.reference is not None:
        instance.reference.save()
