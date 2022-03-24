from django.db import models
from django.db.models.signals import post_save
from django.forms import CharField
from django.utils.translation import gettext_lazy as _

import string, random

def id_generator(size=30, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class ShippingQuerySet(models.QuerySet):

    def delete(self, *args, **kwargs):
        for obj in self:
            obj.task.delete()
        super(ShippingQuerySet, self).delete(*args, **kwargs)


class Shipping(models.Model):
    product = models.CharField(max_length=50, null=True, blank=True)
    customer = models.CharField(max_length=50, null=True, blank=True)
    shipping_status = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        ordering = ['-id']
    