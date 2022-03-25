from oscar.apps.shipping import repository

from .models import OrderAndItemCharges


class Repository(repository.Repository):
    def get_available_shipping_methods(self, basket, shipping_addr=None,
                                       **kwargs):
        return self.get_shipping_methods(basket, shipping_addr, **kwargs)

    def get_shipping_methods(self, *args, **kwargs):
        request = kwargs['request']
        methods = OrderAndItemCharges.objects.filter(
            partners__in=request.partners)
        return methods

    def get_default_shipping_method(self, basket, shipping_addr=None, **kwargs):
        methods = self.get_available_shipping_methods(
            basket, shipping_addr, **kwargs).first()
        if not methods:
            raise ValueError(
                'Missing shipping method for partner '
                + str(basket.owner.partner)
            )
        return methods
