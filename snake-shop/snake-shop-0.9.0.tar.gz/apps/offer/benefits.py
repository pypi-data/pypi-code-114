from decimal import Decimal as D
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.utils.functional import cached_property
from oscar.apps.offer.results import BasketDiscount
from oscar.apps.offer import benefits
from oscar.core.loading import get_class
ZERO_DISCOUNT = get_class('offer.results', 'ZERO_DISCOUNT')


def apply_discount(line, discount, quantity, offer=None, incl_tax=None):
    """
    Apply a given discount to the passed basket
    """
    # use OSCAR_OFFERS_INCL_TAX setting if incl_tax is left unspecified.
    incl_tax = incl_tax if incl_tax is not None else settings.OSCAR_OFFERS_INCL_TAX
    line.discount(discount, quantity, incl_tax=incl_tax, offer=offer)


class OfferProductSpecialPriceBenefit(benefits.AbsoluteDiscountBenefit):
    name = 'Sonderpreise dieses Angebots'
    description = 'Die Produkte werden für den im Angebot eingegebenen Preis verkauft.'
    proxy_class = 'apps.offer.benefits.OfferProductSpecialPriceBenefit'
    type = 'special_price'

    @cached_property
    def product_special_price_dict(self):
        qs = self.range.get_sp_range_products()
        return dict(qs.values_list('product_id', 'special_price'))

    def get_applicable_lines(self, offer, basket):
        """
        Attaches the possible discount to the applicable line
        :returns: [(base_price, line, discount),]
        """
        applicable_lines = super().get_applicable_lines(
            offer, basket, self.range)

        for base_price, line in applicable_lines:
            special_price = self.product_special_price_dict.get(line.product.id)
            if special_price:
                yield (base_price, line, special_price)

    #pylint: disable=too-many-arguments, too-many-locals
    def apply(self, basket, condition, offer, discount_amount=None,
              max_total_discount=None, **kwargs):
        """
        This is a modified version of the PercentageDiscountBenefit
        """
        discount_amount_available = max_total_discount
        line_tuples = self.get_applicable_lines(offer, basket)

        discount = D('0.00')
        affected_items = 0
        max_affected_items = self._effective_max_affected_items()

        for base_price, line, special_price in line_tuples:
            affected_items += line.quantity_with_offer_discount(offer)
            if affected_items >= max_affected_items:
                break
            if discount_amount_available == 0:
                break

            quantity_affected = min(
                line.quantity_without_offer_discount(offer),
                max_affected_items - affected_items
            )
            if quantity_affected <= 0:
                break

            product_discount = base_price - special_price
            line_discount = product_discount * quantity_affected

            if discount_amount_available is not None:
                line_discount = min(line_discount, discount_amount_available)
                discount_amount_available -= line_discount

            apply_discount(line, line_discount, quantity_affected, offer)
            affected_items += quantity_affected
            discount += line_discount

        return BasketDiscount(discount)

    class Meta:
        app_label = 'offer'
        proxy = True
        verbose_name = _("Special price benefit")
        verbose_name_plural = _("Special price benefits")


SpecialPriceBenefit = OfferProductSpecialPriceBenefit


from oscar.apps.offer.benefits import *  # @UnusedWildImport @NoMove @IgnorePep8
