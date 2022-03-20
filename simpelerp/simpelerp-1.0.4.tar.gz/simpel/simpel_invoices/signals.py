from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Invoice, InvoiceItem, InvoiceItemBundle


@receiver(post_save, sender=Invoice)
def after_save_invoice(sender, instance, created, **kwargs):
    if instance.qrcodes.first() is None:
        instance.qrcodes.create(name="public_url", qrcode_data=instance.admin_url)


@receiver(post_save, sender=InvoiceItem)
def after_save_invoiceitem(sender, instance, created, **kwargs):
    instance.invoice.save()


@receiver(post_save, sender=InvoiceItemBundle)
def after_save_invoiceitembundle(sender, instance, created, **kwargs):
    instance.item.save()
