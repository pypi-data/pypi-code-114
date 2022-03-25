from decimal import Decimal as D
from datetime import date, timedelta, time
from types import SimpleNamespace
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.utils import timezone
from django.contrib.sites.models import Site
from oscar.apps.shipping import abstract_models
from oscar.core import prices
from oscar.core.utils import datetime_combine
from custom.site_manager import SiteMixin


class ShippingType(models.IntegerChoices):
    DELIVERY = 1, _('Delivery')
    PICKUP = 2, _('Pickup')


class FormFieldsMode(models.IntegerChoices):
    NONE = 0, _('No form')
    FLOOR = 1, _('Floor')
    DELIVERY = 2, _('Delivery')
    FLOOR_AND_DELIVERY = 3, _('Floor and delivery')
    DATE = 4, _('Date')
    DATETIME = 5, _('Date and time')


class OrderAndItemCharges(SiteMixin, abstract_models.AbstractOrderAndItemCharges):
    site = models.ForeignKey(
        Site, verbose_name=_("Site"),
        on_delete=models.CASCADE,
    )
    overwrite_msg = _('Is overwritten if single floors are configured.')

    method_type = models.PositiveSmallIntegerField(
        _('Shipping Type'),
        choices=ShippingType.choices,
        default=ShippingType.DELIVERY,
    )
    form_fields = models.PositiveSmallIntegerField(
        _('Form fields'),
        choices=FormFieldsMode.choices,
        default=FormFieldsMode.NONE,
    )
    next_day_limit = models.TimeField(
        _('Next day limit'),
        help_text=_('Delivery to the next day possible until this time'),
        blank=True, null=True,
    )
    display_order = models.SmallIntegerField(
        _('Display order'), default=0,
    )
    minimum_order_value = models.DecimalField(
        _("Minimum order value"), decimal_places=2, max_digits=12,
        default=D('30.00'),
    )

    # from abstract_models
    price_per_order = models.DecimalField(
        _("Price per order"), decimal_places=2, max_digits=12,
        help_text=overwrite_msg,
        default=D('0.00'),
    )
    price_per_item = models.DecimalField(
        _("Price per item"), decimal_places=2, max_digits=12,
        help_text=overwrite_msg,
        default=D('0.00'),
    )
    # / from abstract_models

    price_per_floor = models.DecimalField(
        _("Price per floor"), decimal_places=2, max_digits=12,
        help_text=overwrite_msg,
        default=D('0.00'),
    )
    price_per_box = models.DecimalField(
        _("Price per box item"), decimal_places=2, max_digits=12,
        help_text=overwrite_msg,
        default=D('0.00'),
    )
    maximum_floor_difference = models.PositiveSmallIntegerField(
        _('Maximum floor difference'),
        help_text=overwrite_msg,
        null=True, blank=True,
    )
    reference = models.CharField(
        _('Reference number'),
        max_length=50,
        help_text=overwrite_msg,
        blank=True, null=True,
    )
    partners = models.ManyToManyField(
        'partner.Partner',
        related_name='shipping_methods',
        blank=True,
    )

    @property
    def earliest_delivery_date(self):
        if self.next_day_limit and self.delivery_needed:
            # Implemented for 4 and 5 only but should work for others, too
            now = timezone.localtime(timezone.now())
            if self.next_day_limit > now.time():
                earliest_date = date.today() + timedelta(days=1)
            else:
                earliest_date = date.today() + timedelta(days=2)
            return datetime_combine(earliest_date, time())
        return None

    @property
    def delivery_needed(self):
        return self.form_fields in (2, 3, 4, 5)

    @property
    def postcode_restricted(self):
        return self.form_fields in (2, 3)

    @property
    def track_floor(self):
        return self.form_fields in (1, 3)

    def delivery_allowed(self, delivery):
        date = bool(delivery.date)
        time = bool(delivery.time)
        target_time = bool(delivery.target_time)
        if self.form_fields in (2, 3):
            return date and time and not target_time
        if self.form_fields == 4:
            return date and not time and not target_time
        if self.form_fields == 5:
            return date and not time and target_time
        return True

    def get_track_floor(self):
        """
        :returns: True if floor number needs to be tracked during checkout
        """
        return self.track_floor or bool(self.get_floor_range())

    def get_reference(self, shipping_address):
        """
        Single floor reference > self.reference > None
        """
        floor_number = getattr(shipping_address, 'floor_number', None)
        if not floor_number:
            return ''

        if self.shipped_floors.exists():
            qs = self.shipped_floors.filter(floor_number=floor_number)
            floor = qs.first()
            if floor.reference:
                return floor.reference

        return self.reference or ''

    #pylint: disable=arguments-differ
    def calculate(self, basket, shipping_address=None):
        """
        use classmethod to select the correct floor price by partner
        """
        if shipping_address is None and not self.precalculatable:
            return prices.Price(
                currency=basket.currency,
                excl_tax=D('0.00'),
                incl_tax=D('0.00'),
            )

        floor_number = getattr(shipping_address, 'floor_number', None)
        if self.shipped_floors.exists():
            qs = self.shipped_floors.filter(floor_number=floor_number)
            floor = qs.first()
            charge = floor.calculate(basket) if floor else D('0.00')
        else:
            charge = D('0.00')
            charge += self.price_per_order
            charge += self.price_per_item * basket.num_items
            if floor_number is not None:  # When precalculating
                charge += self.price_per_floor * floor_number
            charge += self.price_per_box * basket.num_boxes

        return prices.Price(
            currency=basket.currency,
            excl_tax=charge / D('1.19'),
            incl_tax=charge,
        )

    @property
    def precalculatable(self):
        """
        Precalculation is considered as calculating shipping charge without
        knowing the shipping address (before checkout preview).

        Shipping charges can be precalculated if
        - Has no single floor conditions
        - Has no per-floor-price
        """
        return not self.shipped_floors.exists() and not self.price_per_floor

    def get_floor_range(self):
        if self.shipped_floors.exists():
            qs = self.shipped_floors.all()
            return sorted(qs.values_list('floor_number', flat=True))[::-1]

        i = self.maximum_floor_difference
        if not i:
            return list()

        range_list = list(range(-i, i+1)[::-1])
        return range_list

    def get_number_choices(self, basket):
        if not self.maximum_floor_difference:
            return None

        for floor in self.get_floor_range():
            address = SimpleNamespace(floor_number=floor)
            charge = self.calculate(basket, address)
            label = '{}{}'.format(
                self.get_floor_title(floor, short=False),
                f' (+{charge.incl_tax}€)' if charge.incl_tax else '',
            )
            yield (floor, label)

    @staticmethod
    def get_floor_difference(number):
        if number is not None and number < 0:
            number *= -1
        return number

    @staticmethod
    def get_floor_title(floor_number, short=True):
        if floor_number == 0:
            text = 'EG/Aufzug' if short else 'Erdgeschoss oder Aufzug vorhanden'
        elif floor_number < 0:
            suffix = 'UG' if short else ' Untergeschoss'
            text = str(floor_number) + '.' + suffix
        elif floor_number > 0:
            suffix = 'OG' if short else ' Obergeschoss'
            text = str(floor_number) + '.' + suffix
        return text

    def __str__(self):
        method_type = ShippingType(self.method_type)
        return f'{method_type.label} ({self.name})'

    class Meta:
        ordering = ['display_order']
        app_label = 'shipping'
        verbose_name = _("Order and Item Charge")
        verbose_name_plural = _("Order and Item Charges")


class ShippedFloor(models.Model):
    shipping = models.ForeignKey(
        OrderAndItemCharges,
        on_delete=models.CASCADE,
        related_name='shipped_floors'
    )
    floor_number = models.SmallIntegerField(
        _('Floor number'),
    )
    price = models.DecimalField(
        _("Price"), decimal_places=2, max_digits=12,
        default=D('0.00'),
    )
    price_per_item = models.DecimalField(
        _("Price per item"), decimal_places=2, max_digits=12,
        default=D('0.00')
    )
    price_per_box = models.DecimalField(
        _("Price per box item"), decimal_places=2, max_digits=12,
        default=D('0.00')
    )
    reference = models.CharField(
        _('Reference number'),
        max_length=50,
        blank=True, null=True,
    )

    def calculate(self, basket):
        charge = D('0.00')
        charge += self.price
        charge += self.price_per_item * basket.num_items
        charge += self.price_per_box * basket.num_boxes
        return charge

    def __str__(self):
        return str(self.floor_number)

    class Meta:
        verbose_name = _('Shipped floor')
        verbose_name_plural = _('Shipped floors')
        ordering = ['-floor_number']
        constraints = [
            UniqueConstraint(
                fields=['shipping', 'floor_number'],
                name='unique_shipped_floor',
            )
        ]


from oscar.apps.shipping.models import *  # noqa isort:skip
