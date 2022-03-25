from collections import OrderedDict
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.contrib.sites.models import Site


class PaymentmethodSelectionBase(models.Model):
    """
    Created base class because maybe there will be some other type of parent to
    select payment methods (eg. UserAddress)
    """
    site = models.ForeignKey(
        Site, verbose_name=_("Site"),
        on_delete=models.CASCADE,
    )
    PROVIDER_FIELDS = {
        'cash': 'Bar/EC',
        'sepa': 'Sepa',
        'transfer': 'Vorkasse',
        'account': 'Auf Rechnung',
    }

    cash = models.BooleanField('Bar/EC', default=None)
    sepa = models.BooleanField('Sepa', default=None)
    transfer = models.BooleanField('Vorkasse', default=None)
    account = models.BooleanField('Auf Rechnung', default=None)
    reason = models.TextField('Grund')
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='userpaymentselection_created',
        null=True, blank=True
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='userpaymentselection_updated',
        null=True, blank=True
    )
    date_created = models.DateTimeField(
        _("Date created"), auto_now_add=True, db_index=True)

    date_updated = models.DateTimeField(
        _("Date updated"), auto_now=True, db_index=True)

    class Meta:
        abstract = True
        app_label = 'customer'


class UserPaymentSelection(PaymentmethodSelectionBase):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='payment_selection',
    )

    def providers_allowed(self):
        allowed_providers = OrderedDict()
        for field in self.PROVIDER_FIELDS.keys():
            allowed_providers[field] = getattr(self, field)
        return allowed_providers

    def __str__(self):
        allowed_providers = self.providers_allowed()
        return '{}: {}'.format(
            self.user,
            ', '.join((self.PROVIDER_FIELDS[key] for key, val in allowed_providers.items() if val)),
        )

    class Meta:
        verbose_name = _('Payment selection for User')
        verbose_name_plural = _('Payment selections for User')


from oscar.apps.customer.models import *  # noqa isort:skip
