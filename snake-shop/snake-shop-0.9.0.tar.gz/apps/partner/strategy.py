from decimal import Decimal as D
from django.utils.functional import cached_property
from django.db.models import F

from oscar.apps.partner import strategy
from oscar.core.loading import get_class

from apps.catalogue.models import Product
from apps.offer.models import RangeProduct

from .price import Price, BasePrice, SpecialPrice, Deposit
from .models import StockRecord

TaxInclusiveFixedPrice = get_class('partner.prices', 'TaxInclusiveFixedPrice')
UnavailablePrice = get_class('partner.prices', 'Unavailable')
FixedPrice = get_class('partner.prices', 'FixedPrice')
Available = get_class('partner.availability', 'Available')
Unavailable = get_class('partner.availability', 'Unavailable')


class IncludingDbVAT(strategy.FixedRateTax):
    """
    Price policy to charge VAT on the base price
    """
    exponent = D('0.01')  # Default to two decimal places
    quantity = None
    hide_price = False

    @cached_property
    def product_special_price_dict(self):
        qs = RangeProduct.active_special_prices.all()
        return dict(qs.values_list('product_id', 'special_price'))

    @cached_property
    def product_tax(self):
        return dict(
            Product.objects.values_list(
                'id', 'tax__rate'
            )
        )

    def get_tax(self, product, *args):
        return product.tax

    def get_rate(self, product, stockrecord):
        """ Fetches factor from tax eg. Decimal('0.190') """
        return self.product_tax.get(product.id)

    def get_zero_price(self, stockrecord, factor):
        base_price = BasePrice(
            excl=D('0.00'),
            incl=D('0.00'),
            tax=D('0.00'),
            quantity=self.quantity,
        )
        kwargs = {
            'deposit': None,
            'special_price': None,
            'currency': stockrecord.price_currency,
            'factor': factor,
            'quantity': self.quantity,
        }
        return Price(base_price, **kwargs)

    def pricing_policy(self, product, stockrecord):
        if not product.is_public or not stockrecord \
                or stockrecord.price is None:
            return UnavailablePrice()

        rate = self.product_tax.get(product.id)
        factor = rate / 100+ 1

        if self.hide_price:
            return self.get_zero_price(stockrecord, factor)

        base_price_incl = stockrecord.price
        base_price = BasePrice(
            excl=base_price_incl / factor,
            incl=base_price_incl,
            tax=base_price_incl - base_price_incl / factor,
            quantity=self.quantity,
        )

        deposit_incl = product.deposit
        if deposit_incl:
            deposit = Deposit(
                excl=deposit_incl / factor,
                incl=deposit_incl,
                tax=deposit_incl - deposit_incl / factor,
                quantity=self.quantity,
            )
        else:
            deposit = None

        special_price_incl = self.product_special_price_dict.get(product.id)
        if special_price_incl:
            special_price = SpecialPrice(
                excl=special_price_incl / factor,
                incl=special_price_incl,
                tax=special_price_incl - (special_price_incl / factor),
                quantity=self.quantity
            )
        else:
            special_price = None

        kwargs = {
            'deposit': deposit,
            'special_price': special_price,
            'currency': stockrecord.price_currency,
            'factor': factor,
            'quantity': self.quantity,
        }

        eff_price = special_price_incl if special_price_incl \
            else base_price_incl

        if product.weight:
            kwargs['weight_price'] = eff_price / product.weight

        if product.volume:
            kwargs['volume_price'] = eff_price / product.get_volume()

        return Price(base_price, **kwargs)

    def parent_pricing_policy(self, product, children_stock):
        stockrecords = [x[1] for x in children_stock if x[1] is not None]
        if not stockrecords:
            return UnavailablePrice()
        else:
            return self.pricing_policy(product, stockrecords[0])


class DEStrategy(IncludingDbVAT, strategy.StockRequired, strategy.Structured):
    quantity = 1

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        self.hide_price = self.request.user.hide_price

    def annotate_price(self, qs):
        """ This method can be used to annotate the base_price """
        qs = qs.filter(stockrecords__partner__in=self.request.partners)
        qs = qs.annotate(base_price=F('stockrecords__price'))
        return qs

    @cached_property
    def stockrecords(self):
        qs = StockRecord.objects.filter(partner__in=self.request.partners)
        qs = qs.filter(product__is_public=True)
        qs = qs.distinct('product_id')
        return {stockrecord.product_id: stockrecord for stockrecord in qs}

    def select_stockrecord(self, product):
        stockrecord = self.stockrecords.get(product.id, None)
        return stockrecord

    def fetch_for_product(self, product, stockrecord=None):
        stockrecord = self.select_stockrecord(product)
        return super().fetch_for_product(product, stockrecord=stockrecord)

    def fetch_for_line(self, line, stockrecord=None):
        self.quantity = line.quantity
        return super().fetch_for_line(line, stockrecord)

    def availability_policy(self, product, stockrecord):
        return Available() if stockrecord else Unavailable()


class Selector(object):
    def strategy(self, request, **kwargs):
        return DEStrategy(request)
