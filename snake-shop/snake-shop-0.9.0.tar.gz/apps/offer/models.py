from django.utils.translation import gettext_lazy as _
from django.db import models
from django.db.models import Q
from django.utils.functional import cached_property
from django.contrib.sites.models import Site
from filer.fields.image import FilerImageField
from oscar.apps.offer import abstract_models
from oscar.core.loading import get_class

from apps.partner.models import Partner
from apps.offer.managers import ActiveSpecialPriceManager, ActiveSlideManager,\
    ActiveOfferManager
from custom.site_manager import SiteMixin, DefaultSiteManager

from .managers import RangeSiteManager, BrowsableRangeSiteManager
from .slider import Slide


class Range(SiteMixin, abstract_models.AbstractRange):
    site = models.ForeignKey(
        Site, verbose_name=_("Site"),
        on_delete=models.CASCADE,
    )
    objects = RangeSiteManager()
    browsable = BrowsableRangeSiteManager()

    @classmethod
    def get_special_price_range_ids(cls):
        return cls.objects.filter(benefit__type='special_price').values_list(
            'id', flat=True)

    @classmethod
    def get_special_price_ranges(cls):
        return cls.objects.filter(id__in=cls.get_special_price_range_ids())

    @property
    def in_special_price_ranges(self):
        return self.id in self.get_special_price_range_ids()

    def get_sp_range_products(self):
        qs = RangeProduct.active_special_prices.all()
        qs = qs.filter(range=self)
        return qs

    def contains_product(self, product):
        if self.proxy:
            return self.proxy.contains_product(product)
        return product.id in self.all_product_ids

    @cached_property
    def all_product_ids(self):
        return list(self.all_products().values_list('id', flat=True))


class RangeProductSliderMixin(models.Model):
    product = models.ForeignKey(
        'catalogue.Product',
        verbose_name=_('Product'),
        on_delete=models.CASCADE,
        blank=True, null=True,
        help_text='''Aktiviert den Produkt-Slider und das Produkt Angebot.'''
    )
    image = FilerImageField(
        verbose_name='Angebotsslider Bild',
        on_delete=models.SET_NULL, related_name='slider_image',
        help_text='''Aktiviert den Angebots-Slider.''',
        blank=True, null=True,
    )
    cached_slide = models.ImageField(
        verbose_name='Angebotsslider Bild',
        upload_to='cached_slides/',
        editable=False,
        blank=True, null=True,
    )
    title = models.CharField(
        'Preisschild Label', max_length=100, blank=True, null=True,
        help_text=_('Inhalt des Preislabels im Slide. Überschreibt den Titel '
                    'des Produkts (wenn vorhanden).')
    )
    main_title = models.CharField(
        _('Preisschild Überschrift'),
        help_text=_('Wird über dem Preislabel angezeigt, wenn nicht leer'),
        max_length=20,
        default=_('ANGEBOT'),
    )
    sub_title = models.CharField(
        _('Preisschild Untertitel'),
        help_text=_('Wird unter dem Preislabel angezeigt, wenn nicht leer'),
        max_length=20,
        blank=True, null=True,
    )
    link = models.URLField(
        'Angebotsslider Link', max_length=300, blank=True, null=True,
        help_text='''Link des Elements im Angebots-Slider. Überschreibt den Link 
        des Produkts (wenn vorhanden).'''
    )
    top = models.FloatField(
        _('Horizontal %'),
        help_text=_('Horizontale Position des Preislabels'),
        blank=True, null=True,
    )
    left = models.FloatField(
        _('Vertikal %'),
        help_text=_('Vertikale Position des Preislabels'),
        blank=True, null=True,
    )

    def get_title(self):
        """
        self.title or self.product.title or self.image.title
        """
        if self.title:
            return self.title
        elif self.product:
            return self.product.title
        return self.image.label

    def get_link(self):
        """ Do not use directly, use slide element instead """
        return getattr(self.slide, 'link', None)

    @property
    def has_slide(self):
        return self.image is not None

    @property
    def has_product_offer(self):
        return self.product is not None

    @property
    def slide(self):
        return Slide(self)

    @property
    def label(self):
        """ Label is attached to slide """
        if self.slide and self.slide.label and self.slide.label.is_valid:
            return self.slide.label

    @property
    def has_label(self):
        return bool(self.label)

    def __str__(self):
        return self.get_title()

    class Meta:
        abstract = True


class RangeProductSpecialPriceMixin(models.Model):
    special_price = models.DecimalField(
        'Angebotspreis', decimal_places=2, max_digits=12,
        blank=True, null=True,
        help_text='''Sonderpreis, zu welchem das Produkt angeboten wird, wenn 
        das Angebot aktiv ist. Wird im Preislabel angezeigt.''',
    )
    special_price_start = models.DateTimeField(
        _("Start date"),
        blank=True, null=True,
        help_text='Startdatum dieses Produkt-Angebots.'
    )
    special_price_end = models.DateTimeField(
        _("End date"),
        blank=True, null=True,
        help_text='Enddatum dieses Produkt-Angebots.',
    )

    class Meta:
        abstract = True


class RangeProduct(RangeProductSliderMixin, RangeProductSpecialPriceMixin,
                   abstract_models.AbstractRangeProduct):
    """
    This is used in the Special prices and display options inside of offers.
    """
    objects = DefaultSiteManager(field_name='range')
    active_special_prices = ActiveSpecialPriceManager()
    active_slides = ActiveSlideManager()

    class Meta:
        ordering = ['-display_order']
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_product_and_or_image",
                check=(
                    Q(product__isnull=True, image__isnull=False)
                    | Q(product__isnull=False, image__isnull=True)
                    | Q(product__isnull=False, image__isnull=False)
                ),
            ),
            models.UniqueConstraint(
                name='unique_range_product',
                fields=['range', 'product'],
            )
        ]


class Benefit(abstract_models.AbstractBenefit):
    SPECIAL_PRICE = 'special_price'
    TYPE_CHOICES = [
        (SPECIAL_PRICE, 'Produkte dieses Sortiments zum Sonderpreis erhalten'),
        *abstract_models.AbstractBenefit.TYPE_CHOICES,
    ]
    type = models.CharField(
        _("Type"), max_length=128, choices=TYPE_CHOICES, blank=True)

    @property
    def proxy_map(self):
        return {
            **super().proxy_map,
            self.SPECIAL_PRICE: get_class(
                'offer.benefits', 'OfferProductSpecialPriceBenefit'),
            'Special price': get_class(
                'offer.benefits', 'OfferProductSpecialPriceBenefit'),
        }


class ConditionalOffer(abstract_models.AbstractConditionalOffer):
    """
    A Offer needs to be able to have a benefit range for creating Offer-related
    special prices.
    """
    partner = models.ForeignKey(
        Partner,
        on_delete=models.CASCADE,
        blank=True, null=True,
    )
    objects = DefaultSiteManager(field_name='partner')
    active = ActiveOfferManager()

    def is_special_price_offer(self):
        return self.benefit and self.benefit.type == 'special_price'

    @classmethod
    def special_price_offers(cls):
        return cls.active.filter(benefit__type='special_price')


from oscar.apps.offer.models import *  # noqa isort:skip
