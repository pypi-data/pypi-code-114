from decimal import Decimal as D
from django.db import models
from django.utils.translation import gettext_lazy as _
from oscar.apps.basket import abstract_models
from apps.partner.price import Price, Deposit, Discount, Total, SpecialPrice,\
    BasePrice, PriceBase
from apps.partner.strategy import Unavailable


class Basket(abstract_models.AbstractBasket):
    @property
    def num_boxes(self):
        qs = self.lines.filter(product__has_box=True)
        return sum(qs.values_list('quantity', flat=True))

    def all_lines(self):
        """
        Return a cached set of basket lines.

        This is important for offers as they alter the line models and you
        don't want to reload them from the DB as that information would be
        lost.
        """
        if self.id is None:
            return self.lines.none()
        if self._lines is None:
            self._lines = (
                self.lines
                .select_related('product', 'stockrecord', 'product__tax')
                .prefetch_related(
                    'attributes', 'product__images', 'product__stockrecords',
                    #'product__stockrecords__partner'
                ).order_by(self._meta.pk.name))
        return self._lines

    @property
    def price(self):
        return BasePrice(
            excl=self.total_excl_tax_excl_discounts - self.deposit.excl,
            incl=self.total_incl_tax_excl_discounts - self.deposit.incl,
        )

    @property
    def deposit(self):
        deposit_excl_tax = D()
        deposit_incl_tax = D()
        for line in self.lines.all():
            if line.deposit:
                deposit_excl_tax += line.deposit.excl * line.quantity
                deposit_incl_tax += line.deposit.incl * line.quantity
        return Deposit(excl=deposit_excl_tax, incl=deposit_incl_tax)

    @property
    def discount(self):
        Discount(
            excl=self.total_excl_tax_excl_discounts - self.total_excl_tax,
            incl=self.total_incl_tax_excl_discounts - self.total_incl_tax,
        )

    @property
    def total(self):
        return Total(
            incl=self.total_incl_tax,
            excl=self.total_excl_tax,
        )

    @property
    def after_deposit(self):
        return PriceBase(
            incl=self.total.incl - self.deposit.incl,
            excl=self.total.excl - self.deposit.excl,
        )
    price_with_discount_without_deposit = after_deposit

    @property
    def total_price_incl_tax_excl_deposit(self):
        return self._get_total('line_price_incl_tax_excl_deposit')

    def is_over_minimum_price(self, minimum_price, equal=True):
        if equal and self.total_price_incl_tax_excl_deposit == minimum_price:
            return True
        return self.total_price_incl_tax_excl_deposit > minimum_price


class Line(abstract_models.AbstractLine):

    @property
    def price_obj(self):
        return self.purchase_info.price

    @property
    def deposit(self):
        return getattr(self.price_obj, 'deposit', None) # self.price_obj.deposit

    @property
    def price(self):
        return self.price_obj.base_price
    base_price = price

    @property
    def total(self):
        return self.price_obj.total

    @property
    def unit_price_incl_tax_excl_deposit(self):
        return self.price.incl

    @property
    def line_price_incl_tax_excl_deposit(self):
        return self.price.sum.incl

    @property
    def price_breakdown(self):
        """
        If there is a product in the basket that is not available for this
        partner anymore, it is deleted and will throw an error.
        If the customer reloads the page, it will work now.
        """
        #breakdown_prices = self.get_price_breakdown()
        try:
            breakdown_prices = self.get_price_breakdown()
        except RuntimeError:
            if self.pk:
                self.delete()
            return None

        prices = []
        for incl, excl, qty in breakdown_prices:
            if self.product.deposit:
                deposit = Deposit(incl=self.product.deposit, quantity=qty)
                incl -= deposit.incl
                excl -= deposit.excl
            else:
                deposit = None
            base_price = BasePrice(
                incl=self.price.incl, excl=self.price.excl, quantity=qty
            )
            special_price = SpecialPrice(
                incl=incl, excl=excl, quantity=qty
            )
            if special_price == base_price:
                special_price = None
            prices.append(
                Price(
                    base_price,
                    deposit=deposit,
                    special_price=special_price,
                    quantity=qty,
                )
            )
        return prices


from oscar.apps.basket.models import *  # noqa isort:skip
