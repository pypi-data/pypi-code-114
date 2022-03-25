import re
from decimal import Decimal as D

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.postgres.search import SearchVectorField, SearchVector
from django.db.models import Q
from django.core.cache import cache
from django.contrib.sites.models import Site
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.conf import settings

from oscar.apps.catalogue import abstract_models
from oscar.models.fields.slugfield import SlugField
from oscar.apps.catalogue.abstract_models import MissingProductImage
from sync.sync_id import SyncIdMixin
from .managers import SiteProductManager

User = get_user_model()


class Manufacturer(SyncIdMixin, models.Model):
    name = models.CharField(  # hersteller_name
        _('Name'),
        help_text=_('Kurzbezeichnung des Herstellers'),
        max_length=100,
        unique=True,
    )
    address = models.TextField(
        _('Adresszeile 1'),
        max_length=250,
        blank=True, null=True
    )
    url = models.URLField(  # hersteller_url
        blank=True, null=True
    )
    logo = models.ImageField(
        _('Logo'),
        blank=True, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Marke')
        verbose_name_plural = _('Marken')
        ordering = ['name']


class Tax(SyncIdMixin, models.Model):
    name = models.CharField(_('Name'), max_length=50)
    rate = models.DecimalField(
        _("Tax rate"), decimal_places=2, max_digits=12,
        blank=True, null=True, validators=(
            MinValueValidator(D('0.00')),
            MaxValueValidator(D('100.00'))
        )
    )

    @property
    def factor(self):
        return self.get_rate(as_decimal=True) / D('100.0')

    def get_rate(self, as_decimal=False):
        return self.rate if as_decimal else int(self.rate)

    def __str__(self):
        return f'{self.get_rate()}%'

    class Meta:
        verbose_name = _('Steuersatz')
        verbose_name_plural = _('Steuersätze')


class ProductImportMixin(models.Model):
    """ Only for the migration of the old shop, hopefully """
    VPE_CHOICES = (
        (1, '1l'),
        (2, '1.5l'),
        (3, '0.7l'),
        (4, '1KG'),
    )

    vpefactor = models.DecimalField(
        "Grundpreis Faktor", decimal_places=4, max_digits=12,
        blank=True, null=True, validators=(
            MinValueValidator(D('0.00')),
        )
    )

    vpeid = models.PositiveSmallIntegerField(
        "Grundpreis Einheit", choices=VPE_CHOICES,
        blank=True, null=True
        )
    units = ('12er', 'chep', '5er', 'KA', '6er', 'Fa', 'BIB', 'Fl', 'FL',
             'Stk', 'Dose', 'Pre')
    unit_choices = ((x, x) for x in units)

    unit = models.CharField(
        _("Packaging unit"),
        max_length=4,
        choices=unit_choices,
        blank=True, null=True,
    )
    external_reference = models.CharField(
        max_length=10,
        blank=True, null=True,
    )

    class Meta:
        abstract = True


class SearchMixinBase(models.Model):
    search_vector = SearchVectorField(null=True, blank=True)
    search_fields = []  # Needs to be overwritten

    @classmethod
    def normalize_query(cls, query_string,
                        findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                        normspace=re.compile(r'\s{2,}').sub):
        ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
            and grouping quoted words together.
            Example:

            >>> normalize_query('  some random  words "with   quotes  " and   spaces')
            ['some', 'random', 'words', 'with quotes', 'and', 'spaces']
        https://www.julienphalip.com/blog/adding-search-to-a-django-site-in-a-snap/
        '''
        return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

    @classmethod
    def str_to_query(cls, search_str, search_fields):
        query = None # Query to search for every search term
        terms = cls.normalize_query(search_str)
        for term in terms:
            or_query = None # Query to search for a given term in each field
            for field_name in search_fields:
                q = Q(**{"%s__icontains" % field_name: term})
                if or_query is None:
                    or_query = q
                else:
                    or_query = or_query | q
            if query is None:
                query = or_query
            else:
                query = query & or_query
        return query

    @classmethod
    def search(cls, search_str):
        """ Returns queryset of Products """
        search_query = cls.str_to_query(search_str, cls.search_fields)
        return cls.objects.all().filter(search_query)

    @classmethod
    def get_search_vector(cls):
        return SearchVector(*cls.search_fields)

    class Meta:
        abstract = True


class ReusabilityChoices(models.IntegerChoices):
    DISPOSABLE = 0, _('EINWEG')
    REUSABLE = 1, _('MEHRWEG')


class Product(abstract_models.AbstractProduct, ProductImportMixin,
              SearchMixinBase, SyncIdMixin):
    editors = models.ManyToManyField(
        User,
        verbose_name=_('Product Editoren'),
        help_text=_('Diese Benutzer dürfen das Produkt ohne Überprüfung '
                    'editieren'),
        related_name='edited_products',
        blank=True,
    )
    search_fields = ['title', 'slug', 'description']
    tax = models.ForeignKey(
        Tax,
        on_delete=models.CASCADE,
        verbose_name=_("Tax"),
        default=1,
    )
    optional = _('optional')
    container_count = models.PositiveIntegerField(
        _('Container Count'),
        blank=True, null=True,
    )
    deposit = models.DecimalField(
        _("Deposit sum"),
        decimal_places=2,
        max_digits=12,
        blank=True, null=True, validators=(
            MinValueValidator(D('0.00')),
            MaxValueValidator(D('100.00'))
        )
    )
    weight = models.DecimalField(
        _('weight (kg)'),
        decimal_places=4,
        max_digits=12,
        blank=True, null=True, validators=(
            MinValueValidator(D('0.00')),
        )
    )
    volume = models.DecimalField(
        _('Singlevolume in (l)'),
        decimal_places=4,
        max_digits=12,
        blank=True, null=True, validators=(
            MinValueValidator(D('0.00')),
        )
    )
    has_box = models.BooleanField(
        _("Has box"), blank=True, null=True,
        help_text=_("Does this Product has a box (for box discount)?")
    )
    priority = models.SmallIntegerField(
        _('Priority'), default=0,
        help_text=_('Positive and negative Priority for default ordering of the Results'),
    )
    reusability = models.PositiveSmallIntegerField(
        _('Wiederverwertbarkeit'),
        choices=ReusabilityChoices.choices,
        blank=True, null=True,
    )
    manufacturer = models.ForeignKey(
        Manufacturer,
        verbose_name=_('Marke'),
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='products',
    )
    objects = SiteProductManager()
    is_cleaned = False

    @property
    def attached_values(self):
        values = {}  # label: value
        for key in settings.OSCAR_ATTACHED_PRODUCT_FIELDS:
            if key not in getattr(settings, 'OSCAR_DETAILS_DISABLED_FIELDS', []):
                field = self.get_field(key)
                value = getattr(self, key)
                if field.choices:
                    value = dict(field.choices)[value]
                key = self.get_field_label(field)
                if value:
                    if isinstance(value, D):
                        value = str(value).rstrip('0')
                    values[key] = value
        return values

    @staticmethod
    def get_field(code):
        return Product._meta.get_field(code)

    @staticmethod
    def get_field_label(field):
        if field.related_model:
            return str(field.related_model._meta.verbose_name)
        return str(field.verbose_name)

    @property
    def is_reusable(self):
        return self.reusability == ReusabilityChoices.REUSABLE

    def reusability_label(self):
        if self.reusability is not None:
            return ReusabilityChoices(self.reusability).label
        return ''

    def get_absolute_url(self):
        """
        Return a product's absolute URL
        """
        return reverse('catalogue:detail',
                       kwargs={'product_slug': self.slug, 'upc': self.upc})

    @property
    def packaging(self):
        """ 12x 1,0l PET EW 0,15€ Fl.; 1,50€ Ka. """
        packaging = ''
        if self.container_count:
            packaging += str(self.container_count) + 'x '
        if self.volume:
            packaging += str(self.volume).rstrip('0').rstrip('.') + 'l '
        packaging += 'MW ' if self.is_reusable else 'EW '
        if self.deposit:
            packaging += str(self.get_deposit()) + '€ '
        if self.unit:
            packaging += str(self.unit)
        return packaging

    @property
    def has_options(self):
        """
        Oscar method overwritten for performance purpose. Not really tested
        because we don't use options yet.
        """
        return self.product_options.exists()

    @property
    def options(self):
        for option in self.get_product_class().options.all():
            yield option
        for option in self.product_options.all():
            yield option

    def get_container_count(self):
        return self.container_count or 1

    def get_volume(self):
        if self.volume:
            return self.get_container_count() \
                * self.volume.quantize(D('0.00')).normalize()

    def get_weight(self):
        if self.weight:
            return self.weight.quantize(D('0.00')).normalize()

    def get_deposit(self):
        if self.deposit:
            return self.deposit.quantize(D('0.00'))

    @classmethod
    def by_upc(cls, upc):
        return cls.objects.filter(upc=upc).first()

    @classmethod
    def with_box_ids(cls):
        return cache.get_or_set(
            'Product.with_box_ids',
            cls.objects.browsable().filter(has_box=True).values_list(
            'pk', flat=True)
        )

    def get_missing_image(self):
        site = Site.objects.get_current()
        if site and site.configuration.no_image:
            return MissingProductImage(name=site.configuration.no_image.path)
        return super().get_missing_image()

    def clean(self):
        """
        It is important to remove leading zeros because when importing
        serialized products with python csv, it strips leading zeros.
        """
        super().clean()
        if self.upc.startswith('0'):
            new_upc = self.upc.lstrip('0')
            if self.__class__.objects.filter(upc=new_upc).exists():
                msg = _('Artikelnummer existiert ohne führende 0.')
                raise ValidationError(msg)
            self.upc = new_upc
        self.is_cleaned = True

    def save(self, *args, **kwargs):
        if not self.is_cleaned:
            self.clean()
        cache.delete('Product.with_box')
        super().save(*args, **kwargs)


class CategorySearchMixin(SearchMixinBase):
    search_fields = ['name', 'slug', 'meta_description']

    @classmethod
    def search(cls, search_str):
        """
        returns products so result is union-able with result of product.search
        """
        return cls.search_products(search_str)

    class Meta:
        abstract = True


class Category(abstract_models.AbstractCategory, CategorySearchMixin,
               SyncIdMixin):
    slug = SlugField(_('Slug'), max_length=255, db_index=True, unique=True)

    def get_absolute_url(self):
        return reverse('catalogue:category', kwargs={
            'category_slug': self.get_full_slug(),
        })


class AttributeOptionGroup(abstract_models.AbstractAttributeOptionGroup,
                           SyncIdMixin):
    """ sync_id field through SyncIdMixin """


class ProductClass(abstract_models.AbstractProductClass, SyncIdMixin):
    """ sync_id field through SyncIdMixin """


class ProductAttribute(abstract_models.AbstractProductAttribute, SyncIdMixin):
    """ sync_id field through SyncIdMixin """

    @property
    def product_details_enabled(self):
        return self.code not in getattr(
            settings, 'OSCAR_DETAILS_DISABLED_FIELDS', [])


class AttributeOption(abstract_models.AbstractAttributeOption, SyncIdMixin):
    """ sync_id field through SyncIdMixin """


class ProductCategory(abstract_models.AbstractProductCategory, SyncIdMixin):
    """ sync_id field through SyncIdMixin """

class ProductAttributeValue(abstract_models.AbstractProductAttributeValue,
                            SyncIdMixin):
    """ sync_id field through SyncIdMixin """


class ProductImage(abstract_models.AbstractProductImage, SyncIdMixin):
    """ sync_id field through SyncIdMixin """

    def delete(self, *args, **kwargs):
        """
        Can be removed after successful pull request.
        https://github.com/django-oscar/django-oscar/pull/3891
        After deletion refresh product from db to avoid #3890.
        """
        models.Model.delete(self, *args, **kwargs)
        self.product.refresh_from_db()
        for idx, image in enumerate(self.product.images.all()):
            image.display_order = idx
            image.save()


from oscar.apps.catalogue.models import *  # noqa isort:skip
