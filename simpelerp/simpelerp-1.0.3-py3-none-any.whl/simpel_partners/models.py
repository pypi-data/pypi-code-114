from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _
from simpel.simpel_auth.models import LinkedAddress, LinkedContact
from simpel.simpel_core import const
from simpel.simpel_core.abstracts import ParanoidMixin
from simpel.simpel_core.models import NumeratorMixin


class Partner(NumeratorMixin, ParanoidMixin):
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

    addresses = GenericRelation(
        LinkedAddress,
        content_type_field="linked_object_type",
        object_id_field="linked_object_id",
    )
    contacts = GenericRelation(
        LinkedContact,
        content_type_field="linked_object_type",
        object_id_field="linked_object_id",
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

    @cached_property
    def address(self):
        address = getattr(self, "addresses", None)
        if address:
            address = address.filter(primary=True).first()
        return address

    @cached_property
    def balance(self):
        balance_account = self.get_balance_account()
        return 0.00 if balance_account is None else balance_account.balance

    @classmethod
    def get_for_user(cls, user):
        partner, created = cls.objects.get_or_create(user=user, defaults={"name": user.get_full_name()})
        return partner

    def get_balance_account(self):
        try:
            from simpel.simpel_accounts.settings import (
                simpel_accounts_settings as acc_settings,
            )

            ctype = ContentType.objects.get_for_model(self.__class__)
            balance_account = ctype.accounts.get(
                instance_id=self.id,
                account_type__name=acc_settings.NAMES["PARTNER_BALANCE"],
            )
            return balance_account
        except Exception:
            return None

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
        if address_type is not None:
            filters = {"address_type": address_type}
            ret = self.addresses.filter(**filters).first()
        if ret is None:
            ret = self.addresses.filter(primary=True).first()
        if ret is None:
            ret = self.addresses.first()
        return ret

    def get_deliverable_info(self):
        address = self.get_address(address_type=LinkedAddress.DELIVERABLE)
        if address is not None:
            return address.to_dict()
        return dict()

    def pass_delete_validation(self, paranoid, user=None):
        # Prevent delete validation if
        # Customer sales_order in (valid, processed, complete, invoiced) status
        sales_orders = getattr(self, "sales_orders", None)
        if sales_orders is not None:
            so_states = [const.VALID, const.PROCESSED, const.COMPLETE, const.INVOICED]
            active_orders = sales_orders.filter(status__in=so_states).count()
            if active_orders > 0:
                # Set validation error caution
                self.deletion_error_cautions = _("This customer has active sales orders!")
                return False
        # Customer account from 'simpel_accounts.PartnerAccount" balance != 0
        partner_account = getattr(self, "account", None)
        if partner_account is not None and getattr(partner_account, "balance", 0) > 0:
            self.deletion_error_cautions = _("This customer has balance account!")
            return False
        return True
