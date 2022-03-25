from decimal import Decimal as D
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.sites.models import Site
from localflavor.generic.models import IBANField
from oscar.apps.payment import abstract_models
from schwifty.iban import IBAN
from custom.site_manager import SiteMixin


class SourceType(SiteMixin, abstract_models.AbstractSourceType):
    """
    cash = Bar / EC
    Der Fahrer hat ein Gerät für die Kartenzahlung dabei. 

    sepa = SEPA
    SEPA Bankeinzug (Lastschrift).

    transfer = Vorkasse
    Vorkasse mittels Überweisung. Lieferung erfolgt zum nächstmöglichen Termin nach Zahlungseingang. 

    account = Überweisung
    Rechnung mittels Überweisung nach Lieferung. 
    """
    site = models.ForeignKey(
        Site, verbose_name=_("Site"),
        on_delete=models.CASCADE,
    )
    display_order = models.SmallIntegerField(
        _('Display order'), default=0,
    )
    description = models.TextField(
        _("Description"), blank=True
    )
    minimum_order_value = models.DecimalField(
        _("Minimum order value"), decimal_places=2, max_digits=12,
        default=D('30.00'))

    company_only = models.BooleanField(
        _('Only for companies'),
        help_text=_('Only companies can use this provider'),
        default=True,
    )

    bankcard_needed = models.BooleanField(
        _('Customer bankcard needed'),
        help_text=_('Customer needs to include a bankcard during checkout'),
        default=False,
    )
    enabled = models.BooleanField(
        _('Active'),
        help_text=_('Enable or deactivate this provider'),
        default=True,
    )
    partners = models.ManyToManyField(
        'partner.Partner',
        related_name='source_types',
        blank=True,
    )

    # Is set inside ProviderManager get_providers_for_checkout
    is_allowed = False
    form = None
    hint = None
    disallowed_reason = None

    @classmethod
    def for_user(cls, user):
        providers = cls.objects.filter(enabled=True, partners=user.partner)
        if not providers:
            raise ValueError(
                'Missing payment provider for ' + str(user.partner)
            )
        return providers

    def allowed_for_checkout(self, checkout_session, basket):
        is_over_minimum_price = basket.is_over_minimum_price(
            self.minimum_order_value
        )
        if not basket.owner.hide_price and not is_over_minimum_price:
            # Potenzielle Fehlerquelle für falsche Button Texte:
            self.disallowed_reason = _(
                'Die Mindestbestellmenge beträgt %(min)s €' % {
                    'min': self.minimum_order_value,
                })
            result = False
        else:
            result = True
        return result

    def allowed_for_user_address(self, user_address):
        user = user_address.user
        result = False
        if hasattr(user, 'payment_selection'):
            result = getattr(user.payment_selection, self.code, True)  # 

        elif not self.company_only:
            result = True

        elif self.company_only and user_address.is_company:
            result = True
        return result

    def is_free(self):
        return self.charge_incl_tax == D('0.00')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-enabled', 'display_order']
        app_label = 'payment'
        verbose_name = _("Source Type")
        verbose_name_plural = _("Source Types")


class Bankcard(abstract_models.AbstractBankcard):
    """
    card_type = Bankkonto
    name = owner
    number = iban
    """
    expiry_date = models.DateField(_("Expiry Date"), null=True, blank=True)
    number = IBANField(_("IBAN"))

    def prepare_for_save(self):
        pass  # Do not obfuscate saved iban

    @property
    def obfuscated_number(self):
        iban = self.number
        return len(iban[:-4]) * '*' + iban[-4:]

    @property
    def bic(self):
        return IBAN(self.number).bic

    @property
    def bank_short_name(self):
        return self.bic.bank_short_name if self.bic else ''

    @property
    def bank_name(self):
        """ used by machine email """
        return self.bic.bank_name if self.bic else ''

    @property
    def blz(self):
        return int(IBAN(self.number).bank_code) if self.bic else ''

    @property
    def kto(self):
        return int(IBAN(self.number).account_code) if self.bic else ''

    def start_month(self, *args, **kwargs):
        if self.start_date:
            return super().start_date.strftime(*args, **kwargs)

    def expiry_month(self, *args, **kwargs):
        if self.expiry_date:
            return super().expiry_date.strftime(*args, **kwargs)


from oscar.apps.payment.models import *  # noqa isort:skip
