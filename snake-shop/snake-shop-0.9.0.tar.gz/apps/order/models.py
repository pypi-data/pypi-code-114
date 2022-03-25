from decimal import Decimal as D
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.contrib.sites.models import Site
from localflavor.generic.models import IBANField
from schwifty.iban import IBAN
from oscar.apps.order import abstract_models
from oscar.apps.address import abstract_models as abstract_address_models

from apps.address import models as address_models  # import OrderBankAccountMixin
from apps.partner import strategy, price
from custom.site_manager import SiteMixin


class SageIdMixin(models.Model):
    """ Not exactly the same functionality as UserAddress.sage_id:
    This field is set during Checkout and it uses the UserAddress.sage_id
    Look in address.UserAddress for more information
    """
    sage_id = models.PositiveIntegerField(
        'Sage Kunden ID', default=0
    )

    @property
    def sage_customer_number(self):
        if len(str(self.sage_id)) <= 4:
            return f"D39{self.sage_id:04d}"
        return f"D{self.sage_id:06d}"

    @property
    def hash(self):
        return self.generate_hash()

    class Meta:
        abstract = True


class ShippingAddress(abstract_address_models.AbstractShippingAddress,
                      address_models.AddressMixin, SageIdMixin):
    pass


class BillingAddress(abstract_address_models.AbstractBillingAddress,
                     address_models.AddressMixin, SageIdMixin):
    pass


class Order(abstract_models.AbstractOrder, SiteMixin):
    site = models.ForeignKey(
        Site, verbose_name=_("Site"),
        on_delete=models.CASCADE,
    )
    number = models.PositiveBigIntegerField(
        _("Order number"), db_index=True,
    )
    delivery = models.ForeignKey(
        'delivery.Delivery', null=True, on_delete=models.CASCADE
    )
    payment_provider = models.CharField(
        _("Payment provider"), max_length=128, blank=True
    )
    payment_code = models.CharField(
        _("Payment provider code"), blank=True, max_length=128, default=""
    )

    shipping_reference = models.CharField(
        _("Shipping reference"), blank=True, null=True, max_length=128,
        default="",
    )

    total_deposit_incl_tax = models.DecimalField(
        'Pfand (inkl. Steuer)', decimal_places=2, max_digits=12,
    )
    total_deposit_excl_tax = models.DecimalField(
        'Pfand (ohne Steuer)', decimal_places=2, max_digits=12,
    )
    lines_count = models.PositiveSmallIntegerField(default=0)

    # remove /
    owner = models.CharField(
        _("Account owner"), max_length=150, null=True, blank=True
    )
    iban = IBANField(_("IBAN"), null=True, blank=True)

    @property
    def secret_iban(self):
        return self.iban[:3] + len(self.iban[3:-3]) * 'x' + self.iban[-3:]

    @property
    def bic(self):
        return IBAN(self.iban).bic or ''

    @property
    def bank_short_name(self):
        return getattr(self.bic, 'bank_short_name', '')

    @property
    def bank_name(self):
        """ used by machine email """
        return getattr(self.bic, 'bank_name', '')

    @property
    def blz(self):
        return int(IBAN(self.iban).bank_code) if self.bic else ''

    @property
    def kto(self):
        return int(IBAN(self.iban).account_code) if self.bic else ''
    # /remove

    @property
    def price_obj(self):
        return strategy.DEStrategy().pricing_from_order(self)

    @property
    def deposit(self):
        """ Deposit """
        return price.Deposit(
            incl=self.total_deposit_incl_tax,
            excl=self.total_deposit_excl_tax,
        )

    @property
    def discount(self):
        """ Discount """
        return price.Discount(
            incl=self.total_discount_incl_tax,
            excl=self.total_discount_excl_tax,
        )

    @property
    def base_price(self):
        """ Price without anything """
        base_price = price.BasePrice(
            excl=self.total_before_discounts_excl_tax - self.deposit.excl,
            incl=self.total_before_discounts_incl_tax - self.deposit.incl,
        )
        return base_price
    price = base_price

    @property
    def before_discounts(self):
        """ price before discounts """
        return price.PriceBase(
            excl=self.basket_total_before_discounts_excl_tax,
            incl=self.basket_total_before_discounts_incl_tax,
        )

    @property
    def price_with_discount_without_deposit(self):
        return price.PriceBase(
            incl=self.total.incl - self.deposit.incl,
            excl=self.total.excl - self.deposit.excl,
        )

    @property
    def total(self):
        return price.Total(
            excl=self.total_excl_tax,
            incl=self.total_incl_tax,
        )

    @property
    def shipping_price(self):
        return price.PriceBase(
            excl=self.shipping_excl_tax,
            incl=self.shipping_incl_tax,
        )

    @property
    def floor_shipping_incl_tax(self):
        return D('0.00')

    @property
    def payment_incl_tax(self):
        return D('0.00')

    class Meta(abstract_models.AbstractOrder.Meta):
        unique_together = ['site', 'number']


class Line(abstract_models.AbstractLine):
    unit_deposit_incl_tax = models.DecimalField(
        'Artikel Pfand (inkl. Steuer)', decimal_places=2, max_digits=12,
    )
    unit_deposit_excl_tax = models.DecimalField(
        'Artikel Pfand (ohne Steuer)', decimal_places=2, max_digits=12,
    )

    @property
    def price_breakdown(self):
        prices = []
        for incl, excl, qty in self.prices.values_list(
                'price_incl_tax', 'price_excl_tax', 'quantity'):
            if self.product.deposit:
                deposit = price.Deposit(
                    incl=self.unit_deposit_incl_tax,
                    excl=self.unit_deposit_excl_tax,
                    quantity=qty,
                )
                incl -= deposit.incl
                excl -= deposit.excl
            else:
                deposit = None
            base_price = price.BasePrice(
                incl=self.unit_price_incl_tax - self.deposit.incl,
                excl=self.unit_price_excl_tax - self.deposit.excl,
                quantity=qty
            )
            special_price = price.SpecialPrice(
                incl=incl, excl=excl, quantity=qty
            )
            if special_price == base_price:
                special_price = None
            prices.append(
                price.Price(
                    base_price,
                    deposit=deposit,
                    special_price=special_price,
                    quantity=qty,
                )
            )
        return prices

    @property
    def price_obj(self):
        return strategy.DEStrategy().fetch_for_order_line(self)

    @property
    def total(self):
        """ Total price (from db) After discount """
        return price.Total(
            incl=self.line_price_incl_tax / self.quantity,
            excl=self.line_price_excl_tax / self.quantity,
            quantity=self.quantity,
        )

    @property
    def deposit(self):
        """ Deposit only """
        return price.Deposit(
            excl=self.unit_deposit_excl_tax,
            incl=self.unit_deposit_incl_tax,
            quantity=self.quantity,
        )

    @property
    def price(self):
        """ Price without anything
        returns price only (without deposit and discount) """
        return price.BasePrice(
            excl=self.unit_price_excl_tax - self.deposit.excl,
            incl=self.unit_price_incl_tax - self.deposit.incl,
            quantity=self.quantity,
        )

    @property
    def discount(self):
        """ Discount only """
        return price.Discount(
            incl=self.discount_incl_tax / self.quantity,
            excl=self.discount_excl_tax / self.quantity,
            quantity=self.quantity,
        )

    @property
    def before_discount(self):
        return price.PriceBase(
            incl=self.price.incl + self.deposit.incl,
            excl=self.price.excl + self.deposit.excl,
        )

    @property
    def price_with_discount_without_deposit(self):
        return price.PriceBase(
            incl=self.total.incl - self.deposit.incl,
            excl=self.total.excl - self.deposit.excl,
        )


class LinePrice(abstract_models.AbstractLinePrice):
    @property
    def deposit(self):
        return price.Deposit(
            excl=self.line.unit_deposit_excl_tax,  #pylint: disable=no-member
            incl=self.line.unit_deposit_incl_tax,  #pylint: disable=no-member
            quantity=self.quantity,
        )

    @property
    def price(self):
        return price.BasePrice(
            excl=self.price_excl_tax - self.deposit.excl,
            incl=self.price_incl_tax - self.deposit.incl,
            quantity=self.quantity,
        )


class OrderDiscount(abstract_models.AbstractOrderDiscount):
    @property
    def is_line_applied(self):
        """
        As far as known, all basket discounts are applied to the line price
        :returns: True if this discount is applied to the line breakdown price
        """
        return self.is_basket_discount


from oscar.apps.order.models import *  # noqa isort:skip
