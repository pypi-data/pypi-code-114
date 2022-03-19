import datetime

from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from localflavor.generic.models import IBANField, BICField
from sepaxml import SepaDD
from payments import PaymentStatus
from payments.core import provider_factory


class SEPAMandate(models.Model):
    """A SEPA direct debit mandate."""

    payment = models.OneToOneField(settings.PAYMENT_MODEL, on_delete=models.CASCADE, related_name="sepa_mandate")

    mandate_id = models.CharField(verbose_name=_("Mandate ID"), max_length=35, validators=[RegexValidator(regex=r"^[A-Z0-9+?/:().,'-]{1,35}$")])

    account_holder = models.CharField(verbose_name=_("Account holder"), max_length=64)
    iban = IBANField(verbose_name=_("IBAN of bank account"))
    bic = BICField(verbose_name=_("BIC/SWIFT code of bank"))

    date = models.DateField(verbose_name=_("Date mandate was granted"), auto_now_add=True)

    @classmethod
    def as_sepadd(cls, batch=False, instrument="B2C", qs=None, provider=None):
        if qs is None:
            qs = cls.objects.filter(payment__status=PaymentStatus.PREAUTH)

        first_mandate = qs.first()

        if provider is None:
            provider = provider_factory(first_mandate.payment.variant)

        config = {
            "name": provider.creditor,
            "creditor_id": provider.creditor_identifier,
            "IBAN": provider.iban,
            "BIC": provider.bic,
            "batch": batch,
            "currency": first_mandate.payment.currency,
            "instrument": instrument,
        }

        sepa = SepaDD(config, schema="pain.008.001.02", clean=True)

        for mandate in qs:
            if mandate.payment.currency != first_mandate.payment.currency:
                raise TypeError("The queryset contains more than one different currency.")
            if provider_factory(mandate.payment.variant) != provider:
                raise TypeError("The queryset contains more than one different provider/SEPA config.")

            sepa.add_payment(mandate.as_sepaxml_payment())

        return sepa

    def as_sepaxml_payment(self):
        return {
            "name": self.account_holder,
            "IBAN": self.iban,
            "BIC": self.bic,
            "amount": int(self.payment.total * 100),
            "type": "OOFF",  # FRST,RCUR,OOFF,FNAL
            "collection_date": datetime.date.today(),
            "mandate_id": self.mandate_id,
            "mandate_date": self.date,
            "description": self.payment.description,
            "endtoend_id": self.payment.token.replace("-", ""),
        }
