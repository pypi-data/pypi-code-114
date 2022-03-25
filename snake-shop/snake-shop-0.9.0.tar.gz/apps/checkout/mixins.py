import logging
from django.contrib.sites.models import Site
from oscar.apps.checkout import mixins as base_mixins
from oscar.apps.checkout.mixins import OrderDispatcher
from apps.order import models as order_models
from apps.communication.utils import CustomDispatcher
from custom.context_processors import main as context_processor_main
from . import forms

logger = logging.getLogger('oscar.checkout')


class OrderPlacementMixin(base_mixins.OrderPlacementMixin):
    def handle_payment(self, order_number, total, **kwargs):
        if self.bank_account:
            user_address = self.request.user.addresses.get(
                id=self.checkout_session.billing_user_address_id()
            )
            user_address.default_bank_account = self.bank_account
            user_address.save()
        self.add_payment_source(self.source)

    def handle_order_placement(self, order_number, user, basket,
                               shipping_address, shipping_method,
                               shipping_charge, billing_address, order_total,
                               surcharges=None, **kwargs):
        kwargs.update({
            'delivery': self.delivery,
            'payment_code': self.source_type.code,
            'payment_provider': self.source_type.name,
        })
        if self.bank_account:
            kwargs.update({
                'iban': self.bank_account.number,
                'owner': self.bank_account.name,
            })
        result = super().handle_order_placement(order_number, user, basket,
                               shipping_address, shipping_method,
                               shipping_charge, billing_address, order_total,
                               surcharges=surcharges, **kwargs)
        return result

    def handle_successful_order(self, order):
        form = forms.OrderNoteForm(self.checkout_session, self.request.POST)
        if form.is_valid() and form.cleaned_data.get('newsletter_accepted'):
            user = self.request.user
            user.newsletter_accepted = True
            user.save()
        note_text = self.request.POST.get('note')
        if note_text:
            order_models.OrderNote.objects.create(
                order=order, user=self.request.user, note_type='checkout',
                message=note_text
            )

        result = super().handle_successful_order(order)

        order.refresh_from_db()
        self.send_custom_emails(order)
        return result

    def get_message_context(self, order):
        context = context_processor_main(self.request)
        context.update(super().get_message_context(order))
        context['CONFIG'] = Site.objects.get_current()
        context['request'] = self.request
        return context

    def send_custom_emails(self, order):
        site = self.request.site
        ctx = self.get_message_context(order)

        codes = [
            'ORDER_PLACED_MACHINE1',
            'ORDER_PLACED_INTERNAL_WITH_BANK',
            'ORDER_PLACED_INTERNAL_WITHOUT_BANK',
        ]
        if order.payment_code == 'transfer':
            codes.append('ORDER_PLACED_INTERNAL_TRANSFER')

        for code in codes:
            CustomDispatcher(code, site, extra_context=ctx).send()

    def send_order_placed_email(self, order):
        extra_context = self.get_message_context(order)
        dispatcher = OrderDispatcher(logger=logger)
        dispatcher.send_order_placed_email_for_user(order, extra_context)
