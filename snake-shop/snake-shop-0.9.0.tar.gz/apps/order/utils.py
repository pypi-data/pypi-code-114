from decimal import Decimal as D
from django.conf import settings
from django.http.request import HttpRequest
from django.db.models.aggregates import Max
from django.contrib.sites.models import Site
from oscar.apps.order import utils
from apps.order.models import Order


class OrderNumberGenerator(utils.OrderNumberGenerator):
    productive_zero = 100000
    debug_zero = 0

    def order_number(self, basket):
        site = Site.objects.get_current()  # Explicit but maybe unnecessary
        qs = Order.objects.filter(site=site)

        if settings.DEBUG or settings.STAGE != 'PRODUCTIVE':
            qs = qs.filter(number__lt=self.productive_zero)
            min_value = self.debug_zero
        else:
            min_value = self.productive_zero

        qs = qs.filter(number__gte=min_value)
        qs = qs.aggregate(Max('number'))
        value = qs['number__max'] or min_value
        return value + 1


class OrderCreator(utils.OrderCreator):
    def place_order(self, *args, **kwargs):
        if not kwargs['billing_address']:
            kwargs['billing_address'] = kwargs['shipping_address']
        return super().place_order(*args, **kwargs)

    def create_order_model(self, user, basket, shipping_address,
                           shipping_method, shipping_charge, billing_address,
                           total, order_number, status, request=None,
                           surcharges=None, **extra_order_fields):
        assert isinstance(request, HttpRequest)
        total_deposit_incl_tax = D('0.00')
        total_deposit_excl_tax = D('0.00')

        for line in basket.lines.all():
            price = line.purchase_info.price
            quantity = line.quantity
            if price.deposit:
                total_deposit_incl_tax += price.deposit.incl * quantity
                total_deposit_excl_tax += price.deposit.excl * quantity

        shipping_reference = shipping_method.get_reference(shipping_address)

        extra_order_fields.update({
            'total_deposit_incl_tax': total_deposit_incl_tax,
            'total_deposit_excl_tax': total_deposit_excl_tax,
            'lines_count': basket.lines.count(),
            'shipping_reference': shipping_reference,
            'site': request.site,
        })

        # Refresh order number at the latest possible moment:
        order_number = OrderNumberGenerator().order_number(basket)
        order = super().create_order_model(
            user, basket, shipping_address, shipping_method, shipping_charge,
            billing_address, total, order_number, status, request=None,
            surcharges=None, **extra_order_fields
        )
        return order

    def create_line_models(self, order, basket_line, extra_line_fields=None):
        price = basket_line.purchase_info.price
        extra_line_fields = {
            'unit_deposit_incl_tax': \
                price.deposit.incl if price.deposit else D('0.00'),
            'unit_deposit_excl_tax': \
                price.deposit.excl if price.deposit else D('0.00'),
        }
        order_line = super().create_line_models(
            order, basket_line, extra_line_fields
        )
        return order_line
