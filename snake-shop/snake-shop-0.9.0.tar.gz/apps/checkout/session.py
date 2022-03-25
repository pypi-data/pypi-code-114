from django.utils.translation import gettext_lazy as _
from django.urls.base import reverse
from oscar.apps.checkout import session
from oscar.apps.checkout import exceptions

from apps.basket import models as basket_models
from apps.payment import models as payment_models
from apps.shipping.models import OrderAndItemCharges
from apps.address import models as address_models
from delivery import models as delivery_models


class CheckoutSessionMixin(session.CheckoutSessionMixin):
    def build_submission(self, **kwargs):
        """
        Need to recalculate shipping_charge because it needs the
        shipping_address that is not passed by default.
        """
        result = super().build_submission(**kwargs)
        if result['shipping_address'] and result['shipping_method']:
            result['shipping_charge'] = result['shipping_method'].calculate(
                result['basket'],
                shipping_address=result['shipping_address']
            )
            result["order_total"] += result['shipping_charge']
        return result

    def check_shipping_data_is_captured(self, request):
        super().check_shipping_data_is_captured(request)
        if self.shipping_method.delivery_needed:
            if not self.delivery or not self.delivery.is_selectable:
                raise exceptions.FailedPreCondition(
                    url=reverse('checkout:shipping-method'),
                    message=_('Bitte andere Lieferzeit wählen.'),
                )
            if not self.shipping_method.delivery_allowed(self.delivery):
                raise exceptions.FailedPreCondition(
                    url=reverse('checkout:shipping-method'),
                )

    @property
    def delivery(self):
        delivery_id = self.checkout_session.get_delivery()
        if delivery_id:
            result = delivery_models.Delivery.objects.filter(
                id=delivery_id
            ).first()
            return result
        return None

    @property
    def shipping_method(self):
        code = self.checkout_session.shipping_method_code(self.request.basket)
        return OrderAndItemCharges.objects.get(code=code)

    @property
    def basket(self):
        return basket_models.Basket.objects.get(
            pk=self.checkout_session.get_submitted_basket_id()
        )

    @property
    def source_type(self):
        provider_code = self.checkout_session.payment_method()
        return payment_models.SourceType.objects.get(code=provider_code)

    @property
    def source(self):
        source = payment_models.Source(source_type=self.source_type)
        shipping_charge = self.shipping_method.calculate(
            self.basket, self.shipping_address
        )
        source.amount_allocated = self.request.basket.total_incl_tax \
            + shipping_charge.incl_tax
        if self.bank_account:
            source.reference = '{} - {}'.format(
                self.bank_account.name, self.bank_account.number
            )
        return source

    @property
    def bank_account(self):
        bank_account_id = self.checkout_session.get_bank_account()
        if bank_account_id:
            return payment_models.Bankcard.objects.get(
                pk=bank_account_id,
                user=self.request.user,  # For security
            )

    @property
    def shipping_address(self):
        return address_models.UserAddress.objects.get(
            pk=self.checkout_session.shipping_user_address_id()
        )
