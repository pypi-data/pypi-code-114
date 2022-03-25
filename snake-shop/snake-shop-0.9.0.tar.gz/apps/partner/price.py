from decimal import Decimal as D
from decimal import ROUND_DOWN
from oscar.apps.partner import prices
from django.conf import settings
from oscar.core.loading import cached_import_string


class PriceBase:
    def __init__(self, excl=None, incl=None, tax=None, quantity=1,
                 is_sum=False):
        self.is_sum = is_sum
        self._excl = self.clean(excl)
        self._incl = self.clean(incl)
        self._tax = self.clean(tax)
        self.set_quantity(quantity)
        args_len = len([x for x in [excl, incl, tax] if x is not None])
        if args_len >= 3:
            self.validate()
        elif args_len < 2:
            raise AttributeError('Not enough values to calculate Price')

    def set_quantity(self, quantity):
        if not self.is_sum:
            self.sum_quantity = quantity
            self.quantity = 1
            self.qty = 1
            self.create_sum()
        else:
            self.quantity = quantity
            self.qty = quantity

    def create_sum(self):
        kwargs = {
            'excl': self.excl,
            'incl': self.incl,
            'tax': self.tax,
            'quantity': self.sum_quantity,
            'is_sum': True,
        }
        #pylint: disable=attribute-defined-outside-init
        self.sum = self.__class__(**kwargs)

    def clean(self, value):
        if value is not None:
            return D(value).quantize(D('0.00'))

    def validate(self):
        assert self._incl - self._excl == self._tax
        assert self.incl - self.excl == self.tax

    @staticmethod
    def quantize(price):
        rounding_function_path = getattr(
            settings, 'OSCAR_OFFER_ROUNDING_FUNCTION', None
        )
        rounding_function = cached_import_string(rounding_function_path)
        return rounding_function(price)

    @property
    def excl(self):
        if self._excl is None and self.incl and self.tax:
            result = self.incl - self.tax
        else:
            result = self._excl or D('0.00')
        return max(result * self.quantity, D('0.00'))

    @property
    def incl(self):
        if self._incl is None and self.excl and self.tax:
            result = self.excl + self.tax
        else:
            result = self._incl or D('0.00')
        return max(result * self.quantity, D('0.00'))

    @property
    def tax(self):
        if self._tax is None and self.incl and self.excl:
            result = self.incl - self.excl
        else:
            result = self._tax or D('0.00')
        return max(result * self.quantity, D('0.00'))

    @property
    def factor(self):
        if all([self.incl, self.excl]):
            return self.incl / self.excl

    @property
    def factor_pc(self):
        if self.factor:
            return self.quantize(self.factor)

    def __eq__(self, other):
        result = [
            self.quantize(self.incl) == self.quantize(other.incl),
            self.quantize(self.excl) == self.quantize(other.excl),
            self.quantize(self.tax) == self.quantize(other.tax),
        ]
        if self.sum:
            result.append(self.sum.quantity == other.sum.quantity)
        return all(result)

    def __bool__(self):
        return bool(self.excl and self.incl)

    def __str__(self):
        return '{}(excl={},tax={},incl={}{})'.format(
            self.__class__.__name__,
            self.excl,
            self.tax,
            self.incl,
            f',qty={self.quantity}' if self.quantity else '',
        )

    def __repr__(self):
        return str(self)


class SpecialPrice(PriceBase):
    pass


class SpecialPriceWithDeposit(PriceBase):
    pass


class Deposit(PriceBase):
    def __init__(self, excl=None, incl=None, tax=None, **kwargs):
        if not excl:
            excl = self.quantize(incl / D('1.19'))
            tax = incl - excl
        super().__init__(excl=excl, incl=incl, tax=tax, **kwargs)


class Discount(PriceBase):
    pass


class BasePrice(PriceBase):
    pass


class Total(PriceBase):
    pass


class Price(prices.Base):
    """
    This is the Single Price itself that is used in the strategy
    special_price is only for display purposes
    """
    def __init__(self, base_price, weight_price=None, volume_price=None,
                 deposit=None, discount=None, special_price=None,
                 currency=None, factor=None, quantity=1):
        if not isinstance(self, PriceSum):
            self.sum = PriceSum(base_price, **self.__dict__)
            self.sum.quantity = quantity
        self.quantity = 1
        self.base_price = base_price
        #self.price = self.base_price
        self.deposit = deposit
        self._discount = discount
        self._special_price = special_price
        self.currency = currency
        self.retail = True
        self.factor = factor
        self.weight_price = weight_price
        self.volume_price = volume_price
        #self.validate()

    def validate(self):
        assert isinstance(self.base_price, BasePrice)
        assert isinstance(self.deposit, (Deposit, type(None)))
        assert isinstance(self.discount, (Discount, type(None)))
        assert self.incl - self.excl == self.tax
        if self.factor:
            assert (self.incl / self.excl).quantize(D('0.00')) == self.factor

    @property
    def discount(self):
        if self._discount:
            return self._discount
        elif self._special_price:
            return Discount(
                excl=self.base_price.excl - self._special_price.excl,
                incl=self.base_price.incl - self._special_price.incl,
            )

    @property
    def special_price(self):
        if self._special_price:
            return self._special_price
        elif self._discount:
            return Discount(
                excl=self.base_price.excl - self._discount.excl,
                incl=self.base_price.incl - self._discount.incl,
            )

    @property
    def special_price_with_deposit(self):
        if self.deposit:
            incl = self.special_price.incl + self.deposit.incl
            excl = self.special_price.excl + self.deposit.excl
        else:
            incl = self.special_price.incl
            excl = self.special_price.excl

        return SpecialPriceWithDeposit(incl=incl, excl=excl)

    @property
    def total(self):
        return Total(
            incl=self.base_price.incl + self.deposit.incl,
            excl=self.base_price.excl + self.deposit.excl,
        )

    @property
    def exists(self):
        return self.incl_tax is not None and self.excl_tax is not None

    @property
    def is_tax_known(self):
        return self.tax is not None

    @property
    def excl(self):
        if self.deposit:
            return self.base_price.excl + self.deposit.excl
        return self.base_price.excl

    @property
    def tax(self):
        if self.deposit:
            return self.base_price.tax + self.deposit.tax
        return self.base_price.tax

    @property
    def incl(self):
        if self.deposit:
            return self.base_price.incl + self.deposit.incl
        return self.base_price.incl

    @property
    def has_special_price(self):
        return self.special_price is not None

    @property
    def has_deposit(self):
        return self.deposit is not None

    @property
    def effective_price(self):
        return self.base_price.incl

    @property
    def excl_tax_excl_deposit(self):
        return self.base_price.excl

    @property
    def price_tax(self):
        return self.base_price.tax

    @property
    def incl_tax_excl_deposit(self):
        return self.base_price.incl

    @property
    def deposit_excl_tax(self):
        if self.deposit:
            return self.deposit.excl

    @property
    def deposit_tax(self):
        if self.deposit:
            return self.deposit.tax

    @property
    def deposit_incl_tax(self):
        if self.deposit:
            return self.deposit.incl

    @property
    def excl_tax_incl_deposit(self):
        if self.deposit:
            return self.base_price.excl + self.deposit.excl
        return self.base_price.excl

    excl_tax = excl
    incl_tax = incl
    excl_tax_incl_deposit = excl
    incl_tax_incl_deposit = incl


class PriceSum(Price):
    pass
