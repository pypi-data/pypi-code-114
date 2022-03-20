from datetime import timedelta
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.forms import ValidationError
from django.utils import timezone, translation
from django.utils.functional import cached_property
from django_qrcodes.models import LinkedQRCode
from polymorphic.models import PolymorphicModel

from simpel.simpel_auth.models import LinkedAddress
from simpel.simpel_auth.utils import get_activities
from simpel.simpel_core import const
from simpel.simpel_core.abstracts import ParanoidMixin
from simpel.simpel_core.models import (
    CancelMixin,
    CloseMixin,
    CustomGenericForeignKey,
    NumeratorMixin,
    PaidMixin,
    PendingMixin,
    StatusMixin,
    TrashMixin,
    ValidateMixin,
)
from simpel.simpel_core.models.models import BaseSetting
from simpel.simpel_core.models.registries import register_setting
from simpel.simpel_core.models.templates import PathModelTemplate
from simpel.simpel_products.models import Group, Product
from simpel.utils import reverse

from .settings import simpel_invoices_settings as invoices_settings

_ = translation.gettext_lazy

LEN_SHORT = 128
LEN_LONG = 255


def invoice_due_date():
    return timezone.now() + timedelta(days=invoices_settings.INVOICE_EXPIRATION_LIMIT)


@register_setting
class InvoiceSetting(BaseSetting):
    invoice_template = models.ForeignKey(
        PathModelTemplate,
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.SET_NULL,
        verbose_name=_("Invoice Template"),
        help_text=_("Custom Invoice template."),
    )


class InvoiceStatusMixin(
    TrashMixin,
    PendingMixin,
    ValidateMixin,
    CancelMixin,
    PaidMixin,
    CloseMixin,
    StatusMixin,
):
    class Meta:
        abstract = True

    TRASH = const.TRASH
    PENDING = const.PENDING
    VALID = const.VALID
    CANCELED = const.CANCELED
    PAID = const.PAID
    CLOSED = const.CLOSED
    STATUS_CHOICES = (
        (TRASH, _("Trash")),
        (PENDING, _("Pending")),
        (VALID, _("Valid")),
        (CANCELED, _("Canceled")),
        (PAID, _("Paid")),
        (CLOSED, _("Closed")),
    )

    status = models.IntegerField(choices=STATUS_CHOICES, default=const.PENDING)
    date_closed = models.DateTimeField(
        default=None,
        null=True,
        blank=True,
        editable=False,
        verbose_name=_("Date closed"),
    )

    @property
    def trash_ignore_condition(self):
        return self.is_trash

    @property
    def trash_valid_condition(self):
        return self.is_pending or self.is_canceled

    @property
    def validate_ignore_condition(self):
        return self.is_valid or self.is_paid or self.is_closed

    @property
    def validate_valid_condition(self):
        return self.is_pending or self.is_canceled

    @property
    def cancel_ignore_condition(self):
        return self.is_canceled or self.is_paid or self.is_closed

    @property
    def cancel_valid_condition(self):
        return self.is_cancelable

    @property
    def pay_ignore_condition(self):
        return self.is_paid or self.is_closed

    @property
    def pay_valid_condition(self):
        return self.is_valid

    @property
    def close_ignore_condition(self):
        return self.is_payable

    @property
    def close_valid_condition(self):
        return self.is_valid and self.payable == 0


class Invoice(
    PolymorphicModel,
    NumeratorMixin,
    InvoiceStatusMixin,
    ParanoidMixin,
):
    user = models.ForeignKey(
        get_user_model(),
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="invoices",
        verbose_name=_("Created By"),
    )
    group = models.ForeignKey(
        Group,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="invoices",
        verbose_name=_("Group"),
    )
    issued_date = models.DateTimeField(
        default=timezone.now,
        verbose_name=_("Issued date"),
    )
    due_date = models.DateTimeField(
        default=invoice_due_date,
        verbose_name=_("Due date"),
    )

    customer_type = models.ForeignKey(
        ContentType,
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="invoice_customers",
        verbose_name=_("Customer Type"),
    )
    customer_id = models.IntegerField(null=True, blank=True, verbose_name=_("Customer ID"))
    customer = GenericForeignKey("customer_type", "customer_id")

    reference_type = models.ForeignKey(
        ContentType,
        limit_choices_to={"model__in": ["salesorder"]},
        null=True,
        blank=True,
        related_name="invoices",
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
    note = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("Note"),
    )
    data = models.JSONField(
        null=True,
        blank=True,
        verbose_name=_("Extra data"),
    )
    addresses = GenericRelation(
        LinkedAddress,
        content_type_field="linked_object_type",
        object_id_field="linked_object_id",
    )
    qrcodes = GenericRelation(
        LinkedQRCode,
        content_type_field="linked_object_type",
        object_id_field="linked_object_id",
    )
    items_count = models.IntegerField(
        default=0,
        editable=False,
        verbose_name=_("Items Count"),
    )
    total = models.DecimalField(
        default=0,
        max_digits=15,
        decimal_places=2,
        editable=False,
        verbose_name=_("Total"),
    )
    discount = models.DecimalField(
        default=0,
        max_digits=15,
        decimal_places=2,
        verbose_name=_("Discount"),
    )
    downpayment = models.DecimalField(
        default=0,
        max_digits=15,
        decimal_places=2,
        editable=False,
        verbose_name=_("Downpayment"),
    )
    repayment = models.DecimalField(
        default=0,
        max_digits=15,
        decimal_places=2,
        editable=False,
        verbose_name=_("Repayment"),
    )
    refund = models.DecimalField(
        default=0,
        max_digits=15,
        decimal_places=2,
        editable=False,
        verbose_name=_("Refund"),
    )
    payable = models.DecimalField(
        default=0,
        max_digits=15,
        decimal_places=2,
        editable=False,
        verbose_name=_("Payable"),
    )
    paid = models.DecimalField(
        default=0,
        max_digits=15,
        decimal_places=2,
        editable=False,
        verbose_name=_("Paid"),
    )
    grand_total = models.DecimalField(
        default=0,
        max_digits=15,
        decimal_places=2,
        editable=False,
        verbose_name=_("Grand Total"),
    )

    allow_comments = models.BooleanField(default=True)

    doc_prefix = "INV"

    class Meta:
        db_table = "simpel_invoice"
        verbose_name = _("Invoice")
        verbose_name_plural = _("Invoices")
        index_together = (
            "user",
            "group",
            "customer_type",
            "customer_id",
            "status",
        )
        permissions = (
            ("trash_invoice", _("Can trash Invoice")),
            ("validate_invoice", _("Can validate Invoice")),
            ("cancel_invoice", _("Can cancel Invoice")),
            ("close_invoice", _("Can close Invoice")),
            ("import_invoice", _("Can import Invoice")),
            ("export_invoice", _("Can export Invoice")),
        )

    def __str__(self):
        return "%s - %s" % (str(self.inner_id), self.customer)

    @cached_property
    def qrcode(self):
        return self.qrcodes.first()

    @cached_property
    def billing_address(self):
        return self.addresses.filter(address_type=LinkedAddress.BILLING).first()

    @cached_property
    def shipping_address(self):
        return self.addresses.filter(address_type=LinkedAddress.SHIPPING).first()

    @cached_property
    def is_payable(self):
        return self.is_valid and self.payable > 0

    @cached_property
    def is_editable(self):
        return self.is_pending

    @cached_property
    def is_cancelable(self):
        return self.is_pending or (self.is_valid and self.repayments is None)

    @cached_property
    def is_closable(self):
        return self.is_valid and self.payable == 0

    @cached_property
    def downpayments(self):
        # get receipts that reference to this invoice Sales Order
        so_ctype = ContentType.objects.filter(app_label="simpel_sales", model="salesorder").first()
        payments = getattr(so_ctype, "payments", None)
        if payments is not None:
            return payments.filter(reference_id=self.reference_id)
        return None

    @cached_property
    def repayments(self):
        # get receipts that reference to this invoice
        inv_type = ContentType.objects.get_for_model(self.__class__)
        payments = getattr(inv_type, "payments", None)
        if payments is not None:
            return payments.filter(reference_id=self.inner_id)
        return None

    @cached_property
    def payments(self):
        return self.repayments

    @cached_property
    def balance(self):
        # get partner balance account
        if self.customer.balance:
            if self.customer.balance >= self.get_total():
                return self.get_total()
            else:
                return self.customer.balance
        else:
            return Decimal(0.00)

    @cached_property
    def action_logs(self):
        return get_activities(self)[:5]

    @cached_property
    def admin_url(self):
        view_name = "admin:simpel_invoices_invoice_inspect"
        return reverse(view_name, args=(self.id,), host="admin")

    def get_absolute_url(self):
        return reverse(invoices_settings.INVOICE_ABSOLUTE_URL_NAME, kwargs={"pk": self.pk})

    def get_total(self):
        aggregate = self.items.all().aggregate
        return aggregate(total=models.Sum("total"))["total"] or Decimal(0.00)

    def get_downpayment(self):
        downpayment = Decimal("0.00")
        if self.downpayments is not None:
            downpayment = self.downpayments.filter(status=const.APPROVED).aggregate(total=models.Sum("amount"))["total"]
        return downpayment or Decimal("0.00")

    def get_grand_total(self):
        return self.get_total() - self.discount - self.get_downpayment()

    def get_repayment(self):
        repayment = Decimal("0.00")
        if self.repayments is not None:
            repayment = self.repayments.filter(status=const.APPROVED).aggregate(total=models.Sum("amount"))["total"]
        return repayment or Decimal("0.00")

    def get_paid(self):
        return self.get_downpayment() + self.get_repayment()

    def get_payable(self):
        val = self.get_grand_total() - self.get_repayment()
        return Decimal(0.00) if val <= 0 else val

    def get_refund(self):
        refund = self.get_grand_total() - self.get_repayment()
        return Decimal(0.00) if refund >= 0 else (refund * -1)

    def compute(self):
        self.items_count = self.items.count()
        self.total = self.get_total()
        self.downpayment = self.get_downpayment()
        self.grand_total = self.get_grand_total()
        self.repayment = self.get_repayment()
        self.paid = self.get_paid()
        self.payable = self.get_payable()
        self.refund = self.get_refund()

    def clean(self):
        if self.reference_type is not None and self.reference is None:
            raise ValidationError({"reference_id": _("Reference not found.")})
        if self.reference:
            self.group = self.reference.group

    def delete(self, *args, **kwargs):
        if self.qrcodes is not None:
            self.qrcodes.delete()
        if self.addresses is not None:
            self.addresses.delete()
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.compute()
        return super().save(*args, **kwargs)


class InvoiceItem(NumeratorMixin, ParanoidMixin):
    # Reference & Meta Fields
    invoice = models.ForeignKey(
        Invoice,
        related_name="items",
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        related_name="invoice_items",
        null=False,
        blank=False,
        on_delete=models.PROTECT,
    )
    position = models.IntegerField(
        default=0,
        verbose_name=_("position"),
        help_text=_("Enable sortable position"),
    )
    name = models.CharField(
        verbose_name=_("name"),
        max_length=255,
        null=True,
        blank=True,
        db_index=True,
    )
    alias_name = models.CharField(
        verbose_name=_("alias_name"),
        max_length=255,
        null=True,
        blank=True,
        db_index=True,
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name=_("Quantity"),
        validators=[
            MinValueValidator(1, message=_("Minimal value: 1")),
            MaxValueValidator(500, message=_("Maximal value: 500")),
        ],
    )
    price = models.DecimalField(
        default=0,
        max_digits=15,
        decimal_places=2,
        editable=False,
        verbose_name=_("Price"),
    )
    subtotal = models.DecimalField(
        default=0,
        max_digits=15,
        decimal_places=2,
        editable=False,
        verbose_name=_("Sub Total"),
    )
    total = models.DecimalField(
        default=0,
        max_digits=15,
        decimal_places=2,
        editable=False,
        verbose_name=_("Total"),
    )
    note = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("Note"),
    )

    doc_prefix = "INI"

    class Meta:
        db_table = "simpel_invoice_item"
        index_together = ("invoice", "product")
        verbose_name = _("Invoice Item")
        verbose_name_plural = _("Invoice Items")

    def __str__(self):
        return "%s Order #%s" % (self.inner_id, self.invoice.inner_id)

    def get_total_bundles(self):
        return self.bundles.all().aggregate(total=models.Sum("total"))["total"] or 0

    def get_subtotal(self):
        return self.price + self.get_total_bundles()

    def get_total(self):
        return self.get_subtotal() * self.quantity

    def compute(self):
        if self._state.adding and self.product is not None:
            self.name = self.product.name
            self.price = self.product.total_price
        self.subtotal = self.get_subtotal()
        self.total = self.get_total()

    def save(self, *args, **kwargs):
        self.compute()
        return super().save(*args, **kwargs)


class InvoiceItemBundle(ParanoidMixin):
    # Reference & Meta Fields
    position = models.IntegerField(
        default=0,
        verbose_name=_("position"),
        help_text=_("Enable sortable position"),
    )
    item = models.ForeignKey(
        InvoiceItem,
        related_name="bundles",
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name=_("name"),
        max_length=255,
        null=True,
        blank=True,
        db_index=True,
    )
    product = models.ForeignKey(
        Product,
        related_name="invoice_bundles",
        null=False,
        blank=False,
        limit_choices_to={"is_partial": True},
        on_delete=models.PROTECT,
    )
    price = models.DecimalField(
        default=0,
        max_digits=15,
        decimal_places=2,
        editable=False,
        verbose_name=_("Price"),
    )
    total = models.DecimalField(
        default=0,
        max_digits=15,
        decimal_places=2,
        editable=False,
        verbose_name=_("Total"),
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name=_("Quantity"),
        validators=[
            MinValueValidator(1, message=_("Minimal value: 1")),
            MaxValueValidator(500, message=_("Maximal value: 500")),
        ],
    )

    class Meta:
        db_table = "simpel_invoice_item_bundle"
        index_together = ("item", "product")
        verbose_name = _("Invoice Item Bundle")
        verbose_name_plural = _("Invoice Item Bundles")

    def get_total(self):
        return self.price * self.quantity

    def compute(self):
        if self._state.adding and self.product is not None:
            self.name = self.product.name
            self.price = self.product.total_price
        self.total = self.get_total()

    def save(self, *args, **kwargs):
        self.compute()
        return super().save(*args, **kwargs)
