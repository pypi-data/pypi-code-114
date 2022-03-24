import logging
import warnings

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from simpel_contacts.abstracts import AbstractAddress, AbstractContact
from simpel_numerators.models import NumeratorMixin, NumeratorReset

from .managers import PartnerAddressManager

logger = logging.getLogger(__name__)

warnings.simplefilter("default")


class PartnerContact(AbstractContact):
    partner = models.ForeignKey(
        "simpel_partners.Partner",
        on_delete=models.CASCADE,
        related_name="contacts",
        verbose_name=_("Partner"),
    )

    class Meta:
        verbose_name = _("Partner contact")
        verbose_name_plural = _("Partner contacts")


class PartnerAddress(AbstractAddress):
    """
    A partner can have one or more addresses. This can be useful e.g. when
    determining tax which depends on the origin of the shipment.
    """

    partner = models.ForeignKey(
        "simpel_partners.Partner",
        on_delete=models.CASCADE,
        related_name="addresses",
        verbose_name=_("Partner"),
    )

    objects = PartnerAddressManager()

    class Meta:
        verbose_name = _("Partner address")
        verbose_name_plural = _("Partner addresses")

    def get_primary(self):
        return PartnerAddress.objects.get_primary(self.partner)

    def set_as_primary(self, conditional=False):
        old_primary = self.get_primary()
        if old_primary:
            if conditional:
                return False
            old_primary.primary = False
            old_primary.save()
        self.primary = True
        self.save()
        return True

    def save(self, *args, **kwargs):
        if self.get_primary() is None:
            self.primary = True
        super().save(*args, **kwargs)


class Partner(NumeratorMixin):
    PERSONAL = "personal"
    ORGANIZATION = "organization"
    PARTNER_TYPE = [
        (PERSONAL, _("Personal")),
        (ORGANIZATION, _("Organization")),
    ]
    KTP = "KTP"
    SIM = "SIM"
    TDP = "TDP"
    ID_DOCS = (
        (KTP, "Kartu Tanda Penduduk"),
        (SIM, "Surat Izin Mengemudi"),
        (TDP, "Tanda Daftar Perusahaan"),
    )
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.SET_NULL,
        verbose_name=_("user"),
        null=True,
        blank=True,
    )
    partner_type = models.CharField(
        _("Partner type"),
        max_length=255,
        choices=PARTNER_TYPE,
        default=ORGANIZATION,
    )
    doc = models.CharField(
        max_length=5,
        choices=ID_DOCS,
        default=KTP,
        verbose_name=_("Identity Document"),
        help_text="Identity documents",
    )
    idn = models.CharField(
        null=True,
        blank=False,
        max_length=15,
        verbose_name=_("Identification Number"),
        help_text=_("Identification Number"),
    )
    tax_id = models.CharField(
        null=True,
        blank=True,
        max_length=15,
        verbose_name=_("Tax ID"),
        help_text=_("Tax ID"),
    )
    name = models.CharField(
        _("name"),
        max_length=255,
        db_index=True,
        help_text=_("Can be person name/organization etc as needed."),
    )
    text = models.TextField(
        default="No profile information",
        null=True,
        max_length=245,
        blank=True,
        help_text=_("Describe your self/organization profile."),
    )
    # The html version of the user information.
    html = models.TextField(
        null=True,
        max_length=2550,
        blank=True,
        editable=False,
    )
    attachment = models.FileField(
        null=True, blank=True, verbose_name=_("Attachment"), help_text=_("Partner file attachment: PDF format file.")
    )

    is_active = models.BooleanField(
        default=False,
        editable=False,
    )
    is_verified = models.BooleanField(
        default=False,
        editable=False,
    )
    is_customer = models.BooleanField(
        default=True,
        verbose_name=_("Customer"),
    )
    is_supplier = models.BooleanField(
        default=False,
        verbose_name=_("Supplier"),
    )
    joined_at = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )

    modified_at = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )

    doc_prefix = "PRT"
    reset_mode = NumeratorReset.MONTHLY

    class Meta:
        db_table = "simpel_partner"
        verbose_name = _("Partner")
        verbose_name_plural = _("Partners")
        ordering = ("name",)
        permissions = (
            ("import_partner", _("Can import Partner")),
            ("export_partner", _("Can export Partner")),
            ("change_partner_user", _("Can change Partner user account")),
            ("activate_partner", _("Can activate Partner")),
            ("verify_partner", _("Can verify Partner")),
        )

    def __str__(self):
        return self.name

    def format_inner_id(self):
        """Inner ID final format"""
        form = [self.get_doc_prefix(), self.format_date(form="%m%y"), self.format_number()]
        inner_id = "{}.{}.{}".format(*form)
        return setattr(self, self.inner_id_field, inner_id)

    @classmethod
    def get_for_user(cls, user):
        partner, created = cls.objects.get_or_create(user=user, defaults={"name": user.get_full_name()})
        return partner

    def activate(self):
        if not self.is_active and not self.deleted:
            self.is_active = True
            self.save()
        else:
            raise PermissionError(_("Activation failed, make sure this customer is inactive and not deleted"))

    def deactivate(self):
        if self.is_active and not self.deleted:
            self.is_active = False
            self.save()
        else:
            raise PermissionError(_("This customer is active, or deleted"))

    def verify(self):
        if self.is_active and not (self.is_verified and self.deleted):
            self.is_verified = True
            self.save()
        else:
            raise PermissionError(_("This customer is inactive customer"))

    def get_address(self, address_type=None):
        address = None
        if address_type is not None:
            filters = {"address_type": address_type}
            address = self.addresses.filter(**filters).first()
        if address is None:
            address = address = self.addresses.get_primary(self)
        return address

    @cached_property
    def address(self):
        return self.addresses.get_primary(self)

    @cached_property
    def shipping_address(self):
        return self.get_address(address_type=PartnerAddress.SHIPPING)

    @cached_property
    def billing_address(self):
        return self.get_address(address_type=PartnerAddress.BILLING)

    @cached_property
    def deliverable_address(self):
        return self.get_address(address_type=PartnerAddress.DELIVERABLE)

    def get_deliverable_info(self):
        warnings.warn(
            "get_deliverable_info is deprecated, use partner.deleverable_address.to_dict instead",
            DeprecationWarning,
        )
        if self.deliverable_address is not None:
            return self.deliverable_address.to_dict()
        return dict()

    @cached_property
    def balance(self):
        # TODO Move this to real apps
        balance_account = self.get_balance_account()
        return 0.00 if balance_account is None else balance_account.balance

    def get_balance_account(self):
        # TODO Move this to real apps
        try:
            from simpel_journals.settings import simpel_accounts_settings as acc_settings

            ctype = ContentType.objects.get_for_model(self.__class__)
            balance_account = ctype.accounts.get(
                instance_id=self.id,
                account_type__name=acc_settings.NAMES["PARTNER_BALANCE"],
            )
            return balance_account
        except Exception:
            return None
