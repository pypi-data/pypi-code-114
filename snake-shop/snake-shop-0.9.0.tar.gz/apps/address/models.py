""" In diesem Modul werden die Adress Modelle zusammen geführt
ShippingAddress und BillingAddress werden von der Order app benötigt
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.translation import pgettext_lazy
from django.core.validators import MinValueValidator, MaxValueValidator

from phonenumber_field.modelfields import PhoneNumberField
from localflavor.generic.models import IBANField
from schwifty import IBAN

from oscar.apps.address import abstract_models
from oscar.core.compat import AUTH_USER_MODEL

from apps.shipping import models as shipping_models
from delivery import models as delivery_models
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError


class AddressMixin(models.Model):
    """ Default model for all address models """
    _("First line of address")

    phone_number = PhoneNumberField(
        _("Phone number"), blank=True,
        help_text=_("In case we need to call you about your order"))

    floor_number = models.IntegerField(
        verbose_name=_("Choose Floor"),
        blank=True, null=True
    )

    company = models.CharField(
        _("Company"), max_length=255, blank=True, null=True
    )

    is_company = models.BooleanField(
        'Gewerblicher Kunde?',
        blank=True, null=True
    )

    cost_center = models.CharField(
        'Kostenstelle / Ihre Referenz',
        max_length=150,
        blank=True, null=True
    )

    @property
    def floor_title(self):
        """ This is mainly for usage in emails """
        floor_number = self.floor_number or 0
        return shipping_models.OrderAndItemCharges.get_floor_title(floor_number)

    def get_is_company(self):
        return self.is_company

    class Meta:
        abstract = True


class Country(abstract_models.AbstractCountry):
    pass


class UserAddress(abstract_models.AbstractUserAddress, AddressMixin):
    MR, MISS, MRS, MS, DR = ('Mr', 'Miss', 'Mrs', 'Ms', 'Dr')
    TITLE_CHOICES = (
        (MR, _("Mr")),
        #(MISS, _("Miss")),
        (MRS, _("Mrs")),
        #(MS, _("Ms")),
        (DR, _("Dr")),
    )
    default_bank_account = models.ForeignKey(
        'payment.Bankcard',
        on_delete=models.SET_NULL,
        related_name='bankaccounts',
        verbose_name=_("User"),
        null=True, blank=True,
    )
    title = models.CharField(
        pgettext_lazy("Treatment Pronouns for the customer", "Title"),
        max_length=64, choices=TITLE_CHOICES, blank=True
    )
    sage_id = models.PositiveIntegerField(
        'Überschreibe Sage ID',
        help_text='Überschreibe Sage Kunden ID im Shop (ohne D am Anfang eingeben)',
        blank=True, null=True,
    )
    postcode = models.PositiveIntegerField(
        _("Post/Zip-code"), blank=True,
        validators=(
            MinValueValidator(10000, 'Eine Postleitzahl muss größer sein'),
            MaxValueValidator(99999, 'Eine Postleitzahl muss kleiner sein'),
        )
    )

    def populate_alternative_model(self, address_model):
        """
        This method sets the Sage id to billing address
        It sets the sage_id of the copied adress to self.sage_id if true else self.id
        This belongs to both (shipping and billing address) now.
        """
        super().populate_alternative_model(address_model)
        if hasattr(address_model, 'sage_id'):
            address_model.sage_id = self.sage_id or self.id

    @property
    def next_deliveries(self):
        postcode = delivery_models.Postcode.objects.filter(
            postcode=self.postcode
        ).first()
        if postcode:
            return postcode.get_next_deliveries()

    def validate_unique(self, exclude=None):
        self.country = Country.objects.get(iso_3166_1_a2='DE')
        super().validate_unique(exclude=exclude)

    def save(self, *args, **kwargs):
        self.country = Country.objects.get(iso_3166_1_a2='DE')
        super().save(*args, **kwargs)

    def __str__(self):
        return '{}{}{}{}{}{}'.format(
            f'{self.company} ' if self.company else '',
            self.postcode + ' ' if self.postcode else '',
            self.line4 + ', ' if self.line4 else '',
            self.line1 + ', ' if self.line1 else '',
            self.first_name + ' ' if self.first_name else '',
            self.last_name if self.last_name else '',
        )


class OrderBankAccountMixin(models.Model):
    """
    This was originally used as order mixin, too.
    It is now only used for BankAccount
    """
    owner = models.CharField(_("Account owner"), max_length=150)
    iban = IBANField(_("IBAN"))

    @property
    def secret_iban(self):
        return self.iban[:3] + len(self.iban[3:-3]) * 'x' + self.iban[-3:]

    @property
    def bic(self):
        return IBAN(self.iban).bic

    @property
    def bank_short_name(self):
        return self.bic.bank_short_name if self.bic else ''

    @property
    def bank_name(self):
        """ used by machine email """
        return self.bic.bank_name if self.bic else ''

    @property
    def blz(self):
        return int(IBAN(self.iban).bank_code) if self.bic else ''

    @property
    def kto(self):
        return int(IBAN(self.iban).account_code) if self.bic else ''

    class Meta:
        abstract = True


class BankAccount(OrderBankAccountMixin):
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='bankaccounts',
        verbose_name=_("User"),
        null=True, blank=True,
    )
    card_type = models.CharField(
        _("Card Type"), default=_('Bank account'), max_length=128
    )
    deleted = models.BooleanField(default=False)

    class Meta:
        unique_together = [['iban', 'user'],]
        managed = False


from oscar.apps.address.models import *  # noqa isort:skip
