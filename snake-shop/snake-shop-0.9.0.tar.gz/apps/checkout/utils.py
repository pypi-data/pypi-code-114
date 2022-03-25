from oscar.apps.checkout import utils
from apps.payment import models as payment_models


class CheckoutSessionData(utils.CheckoutSessionData):
    def set_delivery(self, delivery):
        if delivery:
            if isinstance(delivery, (str, int)):
                delivery_pk = int(delivery)
            else:
                delivery_pk = delivery.pk
        else:
            delivery_pk = None
        self._set('delivery', 'code', delivery_pk)

    def get_delivery(self):
        return self._get('delivery', 'code')

    def set_bank_account(self, bank_account):
        if isinstance(bank_account, str):
            bank_account_id = int(bank_account)
        if isinstance(bank_account, payment_models.Bankcard):
            bank_account_id = bank_account.pk
        self._set('address', 'bank_account', bank_account_id)

    def get_bank_account(self):
        return self._get('address', 'bank_account')  # int
