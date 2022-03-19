from django import forms
from django.utils.translation import gettext_lazy as _

from localflavor.generic.forms import BICFormField, IBANFormField
from payments.forms import PaymentForm


class PaymentPledgeForm(PaymentForm):
    _confirmation = _("By confirming this form, I pledge to make the payment as agreed with the merchant.")

    confirmation = forms.BooleanField()

    def __init__(
        self,
        data=None,
        action="",
        method="post",
        provider=None,
        payment=None,
        hidden_inputs=True,
        autosubmit=False,
    ):
        super().__init__(data, action, method, provider, payment, hidden_inputs, autosubmit)
        self.fields["confirmation"].label = self._confirmation.format(provider=provider, payment=payment)


class DirectDebitForm(PaymentPledgeForm):
    account_holder = forms.CharField(label=_("Bank account holder"))
    iban = IBANFormField(label=_("IBAN"))
    bic = BICFormField(label=_("BIC / SWIFT code"))

    _confirmation = _("By signing this mandate form, you authorise (A) {provider.creditor} with creditor identifier {provider.creditor_identifier} to send instructions to your bank to debit your account and (B) your bank to debit your account in accordance with the instructions from {provider.creditor}. As part of your rights, you are entitled to a refund from your bank under the terms and conditions of your agreement with your bank. A refund must be claimed within 8 weeks starting from the date on which your account was debited.")
