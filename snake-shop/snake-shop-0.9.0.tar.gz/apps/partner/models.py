from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.functional import classproperty
from django.core.exceptions import ValidationError
from django.contrib.sites.models import Site
from oscar.apps.partner import abstract_models
from oscar.apps.address import abstract_models as address_models
from oscar.models.fields import AutoSlugField
from apps.address.models import Country
from custom.site_manager import SiteMixin


class StockRecord(abstract_models.AbstractStockRecord):
    is_cleaned = False

    def clean(self):
        super().clean()
        if self.price == 0 and self.partner.code == 'default':
            raise ValidationError(_('Preis wird für Standard-Partner benötigt'))
        self.is_cleaned = True

    def save(self, **kwargs):  # pylint: disable=arguments-differ
        if not self.is_cleaned:
            self.clean()
        return super().save(**kwargs)

    class Meta(abstract_models.AbstractStockRecord.Meta):
        ordering = ('product_id', '-partner__priority')


class Partner(SiteMixin, abstract_models.AbstractPartner):
    default_code = 'default'
    default_name = default_code

    site = models.ForeignKey(
        Site, verbose_name=_("Site"),
        on_delete=models.CASCADE,
    )
    code = AutoSlugField(_("Code"), max_length=128, db_index=True,
                         populate_from='name')
    priceless_checkout = models.BooleanField(
        _('Checkout without price'),
        help_text=_(
            'Allow checkout without price for users of this partner group'
        ),
        default=False,
    )
    priority = models.PositiveSmallIntegerField(
        default=0,
    )
    wishlist_as_link = models.BooleanField(
        _('Favoriten als Links'),
        help_text=_('Favoriten werden im Filter als Link angezeigt'),
        default=False,
    )
    @classproperty
    def default(cls):
        """ DEPRECATED - Don't use anymore, find better solutions """
        site = Site.objects.get_current()
        return cls.objects.filter(site=site, code=cls.default_code).first()

    def save(self, *args, **kwargs):
        if self.code == self.default_code:
            self.priority = 0
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.site}>{self.name}'

    class Meta(abstract_models.AbstractPartner.Meta):
        ordering = ('-priority', 'name', 'code')
        unique_together = (
            ('site', 'priority'),
            ('site', 'code'),
        )


class PartnerAddress(address_models.AbstractPartnerAddress):
    def save(self, *args, **kwargs):
        if not self.country_id:
            self.country = Country.objects.get(iso_3166_1_a2='DE')
        return super().save(*args, **kwargs)


from oscar.apps.partner.models import *  # noqa isort:skip
