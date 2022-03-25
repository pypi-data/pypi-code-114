import datetime

from django.dispatch import receiver
from django.db.models.signals import post_save

from document.models import Document

from .models import Customer


@receiver(post_save, sender=Document)
def handler_save_document(sender, instance, created, **kwargs):
    if created:
        forbidden = True
        if instance.owner.is_staff:
            forbidden = False
        elif instance.owner.owner.count() < 3:
            forbidden = False
        else:
            customer = Customer.objects.filter(user=instance.owner).first()
            if not customer:
                pass
            elif customer.cancelation_date:
                if customer.cancelation_date > datetime.date.today():
                    forbidden = False
                else:
                    customer.delete()
            else:
                forbidden = False
        if forbidden:
            instance.delete()
