from urllib.parse import ParseResult
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from oscarapi.models import ApiKey
from apps.catalogue.models import Product


class TimestampMixin(models.Model):
    date_created = models.DateTimeField(
        _('Erstelldatum'),
        auto_now_add=True,
    )
    date_updated = models.DateTimeField(
        _('Änderungsdatum'),
        auto_now=True,
    )
    class Meta:
        abstract=True


class Schema(models.TextChoices):
    HTTPS = 'https', _('Https')
    HTTP = 'http', _('Http (Nur für Dev verwenden!)')


class Shop(TimestampMixin, models.Model):
    enabled = models.BooleanField(
        _('Aktiviert'),
        help_text=_('Wenn deaktiviert, wird auf diesem Shop kein sync '
                    'durchgeführt'),
        default=True,
    )
    master = models.BooleanField(
        _('Master'),
        help_text=_('Dies ist die Verbindung zur Master Api'),
        default=False,
        unique=True,
    )
    key = models.OneToOneField(
        ApiKey,
        on_delete=models.CASCADE,
        help_text=_('Der API Schlüssel muss mit dem im slave übereinstimmen'),
        related_name='shop',
    )
    domain = models.CharField(
        _('Domain'),
        help_text=_('Domain ohne Schema und Pfad (z.B. master-shop.de)'),
        max_length=100,
    )
    schema = models.CharField(
        _('Schema'),
        max_length=10,
        choices=Schema.choices,
        default=Schema.HTTPS,
    )
    sync_delete = models.BooleanField(
        _('Löschen bei Sync'),
        help_text=_('Löschen von Objekten während Synchronisierung erlauben'),
        default=False,
    )

    @property
    def api_url(self):
        url_kwargs={
            'scheme': self.schema,
            'netloc': self.domain,
            'path': '', 'query': '', 'params': '', 'fragment': '',
        }
        return ParseResult(**url_kwargs).geturl()

    def get_products(self):
        return Product.objects.all()

    def __str__(self):
        return self.domain

    class Meta:
        verbose_name = _('Verbundener Shop')
        verbose_name_plural = _('Verbundene Shops')

