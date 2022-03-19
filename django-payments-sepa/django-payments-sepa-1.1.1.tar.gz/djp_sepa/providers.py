from payments import PaymentStatus, RedirectNeeded
from payments.core import BasicProvider

from .forms import DirectDebitForm, PaymentPledgeForm
from .models import SEPAMandate


class PaymentPledgeProvider(BasicProvider):
    """Payment pledge provder.

    The customer pledges to make the payment for manual handling in an arbitrary way.
    """

    def get_form(self, payment, data=None):
        if payment.status == PaymentStatus.WAITING:
            payment.change_status(PaymentStatus.INPUT)

        form = PaymentPledgeForm(data=data, hidden_inputs=False, provider=self, payment=payment)
        if form.is_valid():
            payment.change_status(PaymentStatus.PREAUTH)
            raise RedirectNeeded(payment.get_success_url())

        return form

    def capture(self, payment, amount=None):
        payment.change_status(PaymentStatus.CONFIRMED)
        return amount

    def release(self, payment):
        return None

    def refund(self, payment, amount=None):
        return amount or 0


class DirectDebitProvider(BasicProvider):
    """SEPA direct debit provder.

    This provider requests the customer to provide a direct debit mandate.
    """

    def __init__(self, creditor, creditor_identifier, iban, bic, capture=False):
        super().__init__(capture)

        self.creditor = creditor
        self.creditor_identifier = creditor_identifier
        self.iban = iban
        self.bic = bic

    def get_form(self, payment, data=None):
        if payment.status == PaymentStatus.WAITING:
            payment.change_status(PaymentStatus.INPUT)

        form = DirectDebitForm(data=data, hidden_inputs=False, provider=self, payment=payment)
        if form.is_valid():
            self.release(payment)
            SEPAMandate.objects.create(payment=payment, account_holder=form.cleaned_data["account_holder"], iban=form.cleaned_data["iban"], bic=form.cleaned_data["bic"])

            payment.change_status(PaymentStatus.PREAUTH)
            raise RedirectNeeded(payment.get_success_url())

        return form

    def capture(self, payment, amount=None):
        payment.change_status(PaymentStatus.CONFIRMED)
        return amount

    def release(self, payment):
        SEPAMandate.objects.filter(payment=payment).delete()

    def refund(self, payment, amount=None):
        return amount or 0
