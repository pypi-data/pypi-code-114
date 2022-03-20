from functools import cached_property

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _  # NOQA
from polymorphic.models import PolymorphicModel

from simpel.simpel_core import const
from simpel.simpel_core.models import CustomGenericForeignKey, NumeratorMixin, mixins

LEN_SHORT = 128
LEN_LONG = 255


class PaymentGateway(PolymorphicModel):
    class Meta:
        db_table = "simpel_payment_gateway"
        verbose_name = _("Gateway")
        verbose_name_plural = _("Gateways")

    PERCENT = "PERCENT"
    NOMINAL = "NOMINAL"

    RATE_METHOD = (
        (PERCENT, _("Percentage")),
        (NOMINAL, _("Nominal")),
    )

    thumbnail = models.ImageField(
        verbose_name="Icon",
        null=True,
        blank=True,
    )
    name = models.CharField(
        max_length=LEN_SHORT,
        verbose_name=_("Name"),
    )
    rate_method = models.CharField(
        max_length=LEN_SHORT,
        default=PERCENT,
        choices=RATE_METHOD,
        verbose_name=_("Rate method"),
    )
    transfer_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)],
        verbose_name=_("Transfer fee"),
    )
    auto_confirm = models.BooleanField(
        default=False,
        verbose_name=_("Auto confirmation"),
        help_text=_("Customer should inform payment manual if false"),
    )
    active = models.BooleanField(default=True)

    @cached_property
    def opts(self):
        return self.get_real_instance_class()._meta

    @cached_property
    def specific(self):
        return self.get_real_instance()

    def receive_payment(self):
        """Receive payment will create Payment"""
        raise NotImplementedError("%s must implement make_payment method")

    def clean(self):
        if self.rate_method == PaymentGateway.PERCENT and self.transfer_fee > 100:
            raise ValidationError({"transfer_fee": _("%s is not valid percent number") % self.transfer_fee})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return "%s" % (self.specific.__str__())


class CashGateway(PaymentGateway):
    class Meta:
        db_table = "simpel_payment_gateway_cash"
        verbose_name = _("Cash Payment")
        verbose_name_plural = _("Cash Payment")

    def __str__(self):
        return "%s" % (self.name)


class ManualTransferGateway(PaymentGateway):
    class Meta:
        db_table = "simpel_payment_gateway_manual_transfer"
        verbose_name = _("Manual Transfer")
        verbose_name_plural = _("Manual Transfers")

    bank_name = models.CharField(
        max_length=LEN_SHORT,
        verbose_name=_("Bank Name"),
    )
    bank_branch_office = models.CharField(
        max_length=LEN_SHORT,
        verbose_name=_("Branch Office"),
    )
    bank_account = models.CharField(
        max_length=LEN_SHORT,
        verbose_name=_("Account number"),
    )
    bank_holder_name = models.CharField(
        max_length=LEN_SHORT,
        verbose_name=_("Account holder"),
    )

    def __str__(self):
        return "%s (%s)" % (self.name, self.bank_holder_name)


class PaymentActionMixin(
    mixins.PendingMixin,
    mixins.ValidateMixin,
    mixins.CancelMixin,
    mixins.ApproveMixin,
    mixins.RejectMixin,
):

    STATUS_CHOICES = [
        (const.PENDING, _("Pending")),
        (const.VALID, _("Validated")),
        (const.REJECTED, _("Rejected")),
        (const.APPROVED, _("Approved")),
        (const.CANCELED, _("Canceled")),
    ]
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=const.PENDING,
        verbose_name=_("Status"),
    )

    class Meta:
        abstract = True

    @cached_property
    def validate_ignore_condition(self):
        return self.is_valid or self.is_approved

    @cached_property
    def validate_valid_condition(self):
        return self.is_pending or self.is_rejected

    @cached_property
    def approve_ignore_condition(self):
        return self.is_approved

    @cached_property
    def approve_valid_condition(self):
        return self.is_valid or self.is_canceled

    @cached_property
    def reject_ignore_condition(self):
        return self.is_rejected or self.is_approved

    @cached_property
    def reject_valid_condition(self):
        return self.is_valid or self.is_canceled

    @cached_property
    def cancel_ignore_condition(self):
        return self.is_canceled

    @cached_property
    def cancel_valid_condition(self):
        return self.is_approved


class Payment(PolymorphicModel, PaymentActionMixin, NumeratorMixin):

    RECEIPT = "RCP"
    WITHDRAW = "CWD"
    PAYMENT_TYPE_CHOICES = (
        (RECEIPT, _("Receipt")),
        (WITHDRAW, _("Withdraw")),
    )

    user = models.ForeignKey(
        get_user_model(),
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="payments",
        verbose_name=_("Created By"),
    )
    type = models.CharField(
        max_length=15,
        choices=PAYMENT_TYPE_CHOICES,
        default=RECEIPT,
        verbose_name=_("Type"),
    )

    # Reference Contentype
    reference_type = models.ForeignKey(
        ContentType,
        limit_choices_to={"model__in": ["invoice", "salesorder"]},
        null=True,
        blank=True,
        related_name="payments",
        on_delete=models.SET_NULL,
        help_text=_(
            "Please select reference type, then provide valid inner id as reference, otherwise leave it blank."
        ),
    )
    reference_id = models.CharField(
        max_length=255,
        null=True,
        blank=False,
        verbose_name=_("Reference"),
    )
    reference = CustomGenericForeignKey(
        "reference_type",
        "reference_id",
        "inner_id",
    )
    gateway = models.ForeignKey(
        PaymentGateway,
        null=True,
        blank=True,
        related_name="payments",
        on_delete=models.SET_NULL,
        help_text=_("Payment gateway"),
    )
    amount = models.DecimalField(
        default=0,
        max_digits=15,
        decimal_places=2,
        verbose_name=_("Amount"),
    )
    note = models.CharField(
        default="",
        max_length=LEN_LONG,
        null=True,
        blank=True,
        verbose_name=_("Memo"),
    )

    class Meta:
        db_table = "simpel_payment"
        verbose_name = _("Payment")
        verbose_name_plural = _("Payments")
        permissions = (
            ("validate_payment", "Can validate Payment"),
            ("approve_payment", "Can approve Payment"),
            ("reject_payment", "Can reject Payment"),
            ("cancel_payment", "Can cancel Payment"),
            ("export_payment", "Can export Payment"),
            ("import_payment", "Can import Payment"),
        )

    def __str__(self):
        return self.inner_id

    @cached_property
    def opts(self):
        return self.get_real_instance_class()._meta

    @cached_property
    def specific(self):
        return self.get_real_instance()

    @cached_property
    def timesince(self, now=None):
        """
        Shortcut for the ``django.utils.timesince.timesince`` function of the
        current timestamp.
        """
        from django.utils.timesince import timesince as timesince_

        return timesince_(self.created_at, now)

    @cached_property
    def is_editable(self):
        return self.is_pending

    @cached_property
    def is_cancelable(self):
        return self.is_approved

    def get_doc_prefix(self):
        return self.type

    def clean(self):
        if self.reference_type is not None and self.reference is None:
            raise ValidationError({"reference_id": _("Reference not found.")})
        if self.reference:
            if self._state.adding and not self.reference.is_payable:
                raise ValidationError({"reference_id": _("Reference status is not payable.")})
            if self.amount > self.reference.payable:
                raise ValidationError(
                    {"amount": _("Amount greater than %s payable: %s" % (self.reference, self.reference.payable))}
                )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
