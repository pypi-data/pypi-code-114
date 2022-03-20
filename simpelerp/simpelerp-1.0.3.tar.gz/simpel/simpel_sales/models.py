from datetime import timedelta
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _
from django_qrcodes.models import LinkedQRCode
from polymorphic.models import PolymorphicModel

from simpel.simpel_auth.models import LinkedAddress
from simpel.simpel_auth.utils import get_activities
from simpel.simpel_core import const
from simpel.simpel_core.abstracts import ParanoidMixin
from simpel.simpel_core.models import BaseSetting, NumeratorMixin
from simpel.simpel_core.models.registries import register_setting
from simpel.simpel_core.models.templates import PathModelTemplate
from simpel.simpel_products.models import Group, Product
from simpel.utils import reverse

from .managers import OrderItemBundleManager, OrderItemManager, OrderManager
from .mixins import SalesOrderActionMixin, SalesQuotationActionMixin
from .settings import simpel_sales_settings as sales_settings


def sales_order_expired():
    return timezone.now() + timedelta(
        days=sales_settings.SALESORDER_EXPIRATION_LIMIT,
    )


@register_setting
class SalesSetting(BaseSetting):

    salesorder_template = models.ForeignKey(
        PathModelTemplate,
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.SET_NULL,
        verbose_name=_("Order Template"),
        help_text=_("Custom Order template."),
    )
    salesorder_expiration = models.IntegerField(
        null=True,
        blank=True,
        verbose_name=_("Order Expiration"),
    )
    salesorder_signer_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("Order Signer"),
    )
    salesorder_signer_position = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("Order Signer Position"),
    )
    salesorder_signer_eid = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("Order Signer EID"),
    )

    # Sales Quotation Settings
    salesquotation_template = models.ForeignKey(
        PathModelTemplate,
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.SET_NULL,
        verbose_name=_("Quotation Template"),
        help_text=_("Custom Quotation template."),
    )
    salesquotation_expiration = models.IntegerField(
        null=True,
        blank=True,
        verbose_name=_("Quotation Expiration"),
    )
    salesquotation_signer_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("Quotation Signer"),
    )
    salesquotation_signer_position = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("Quotation Signer Position"),
    )
    salesquotation_signer_eid = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("Quotation Signer EID"),
    )


class SalesQuotation(
    PolymorphicModel,
    NumeratorMixin,
    SalesQuotationActionMixin,
    ParanoidMixin,
):

    user = models.ForeignKey(
        get_user_model(),
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="quotations",
        verbose_name=_("User"),
    )
    # Reference & Meta Fields
    group = models.ForeignKey(
        Group,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="salesquotations",
        verbose_name=_("Group"),
    )
    expired_at = models.DateTimeField(
        default=sales_order_expired,
        null=True,
        blank=True,
    )

    customer_type = models.ForeignKey(
        ContentType,
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="salesorder_customers",
        verbose_name=_("Customer Type"),
    )
    customer_id = models.IntegerField(null=True, blank=True, verbose_name=_("Customer ID"))

    customer = GenericForeignKey("customer_type", "customer_id")

    discount = models.DecimalField(
        default=0,
        max_digits=15,
        decimal_places=2,
        verbose_name=_("Discount"),
    )
    reference = models.CharField(
        _("PO Number"),
        max_length=50,
        null=True,
        blank=True,
        help_text=_(
            "Purchase Order number.",
        ),
    )
    note = models.TextField(
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
    total = models.DecimalField(
        default=0,
        max_digits=15,
        decimal_places=2,
        editable=False,
        verbose_name=_("Total"),
    )
    grand_total = models.DecimalField(
        default=0,
        max_digits=15,
        decimal_places=2,
        editable=False,
        verbose_name=_("Grand Total"),
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

    allow_comments = models.BooleanField(default=True)

    doc_prefix = "SQ"
    objects = OrderManager()

    class Meta:
        db_table = "simpel_sales_quotation"
        verbose_name = _("Sales Quotation")
        verbose_name_plural = _("Sales Quotations")
        index_together = (
            "user",
            "group",
            "customer_type",
            "customer_id",
            "status",
        )
        permissions = (
            ("import_salesquotation", _("Can import Sales Quotation")),
            ("export_salesquotation", _("Can export Sales Quotation")),
            ("validate_salesquotation", _("Can validate Sales Quotation")),
            ("process_salesquotation", _("Can process Sales Quotation")),
            ("accept_salesquotation", _("Can accept Sales Quotation")),
        )

    def __str__(self):
        return "%s - %s" % (str(self.inner_id), self.customer)

    @cached_property
    def opts(self):
        return self.__class__._meta

    @cached_property
    def admin_url(self):
        view_name = "admin:simpel_sales_salesquotation_inspect"
        return reverse(view_name, args=(self.id,), host="admin")

    def get_absolute_url(self):
        from .settings import simpel_sales_settings as sales_settings

        return reverse(sales_settings.SALESQUOTATION_ABSOLUTE_URL_NAME, kwargs={"pk": self.pk})

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
    def action_logs(self):
        return get_activities(self)[:5]

    @cached_property
    def items_count(self):
        return self.get_items_count()

    @cached_property
    def total_items(self):
        return self.get_total_items()

    def get_items_count(self):
        return self.items.count()

    def get_total_items(self):
        return self.items.all().aggregate(total=models.Sum("total"))["total"] or 0

    def get_grand_total(self):
        return self.total - self.discount

    def compute(self):
        self.total = self.get_total_items()
        self.grand_total = self.get_grand_total()

    def delete(self, *args, **kwargs):
        if self.qrcodes is not None:
            self.qrcodes.delete()
        if self.addresses is not None:
            self.addresses.delete()
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.compute()
        return super().save(*args, **kwargs)


class SalesQuotationItem(NumeratorMixin, ParanoidMixin):
    # Reference & Meta Fields
    salesquotation = models.ForeignKey(
        SalesQuotation,
        related_name="items",
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        related_name="quotation_items",
        limit_choices_to={"is_sellable": True},
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
        editable=False,
        db_index=True,
    )
    alias_name = models.CharField(
        verbose_name=_("alias name"),
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
    note = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("Note"),
    )

    price = models.DecimalField(
        default=0,
        max_digits=15,
        decimal_places=2,
        editable=False,
        verbose_name=_("Price"),
    )
    total_bundles = models.DecimalField(
        default=0,
        max_digits=15,
        decimal_places=2,
        editable=False,
        verbose_name=_("Total Bundles"),
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

    deliverable_informations = GenericRelation(
        LinkedAddress,
        content_type_field="linked_object_type",
        object_id_field="linked_object_id",
    )

    doc_prefix = "QUI"

    class Meta:
        db_table = "simpel_sales_quotation_item"
        ordering = ("position",)
        index_together = ("salesquotation", "product")
        verbose_name = _("Quotation Item")
        verbose_name_plural = _("Quotations Items")
        permissions = (
            ("import_salesquotationitem", _("Can import Sales Quotation Item")),
            ("export_salesquotationitem", _("Can export Sales Quotation Item")),
        )

    def __str__(self):
        return "#%s:%s - %s" % (self.inner_id, self.salesquotation.inner_id, self.name)

    @cached_property
    def opts(self):
        return self.__class__._meta

    @cached_property
    def deliverable_information(self):
        return self.deliverable_informations.filter(address_type=LinkedAddress.DELIVERABLE).first()

    def get_total_bundles(self):
        return self.bundles.all().aggregate(total=models.Sum("total"))["total"] or 0

    def get_subtotal(self):
        return self.price + self.get_total_bundles()

    def get_total(self):
        return self.get_subtotal() * self.quantity

    def compute(self):
        if self._state.adding and self.product is not None:
            self.name = self.product.name
            self.price = self.product.specific.price
        self.total_bundles = self.get_total_bundles()
        self.subtotal = self.get_subtotal()
        self.total = self.get_total()

    def save(self, *args, **kwargs):
        self.compute()
        return super().save(*args, **kwargs)


class SalesQuotationItemBundle(NumeratorMixin, ParanoidMixin):
    # Reference & Meta Fields
    position = models.IntegerField(
        default=0,
        verbose_name=_("position"),
        help_text=_("Enable sortable position"),
    )
    item = models.ForeignKey(
        SalesQuotationItem,
        related_name="bundles",
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        related_name="quotation_item_bundles",
        null=False,
        blank=False,
        limit_choices_to={
            "is_partial": True,
            "is_sellable": True,
        },
        on_delete=models.PROTECT,
    )
    name = models.CharField(
        verbose_name=_("name"),
        max_length=255,
        null=True,
        blank=True,
        db_index=True,
    )
    price = models.DecimalField(
        default=0,
        max_digits=15,
        decimal_places=2,
        editable=False,
        verbose_name=_("Price"),
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name=_("Quantity"),
        validators=[
            MinValueValidator(1, message=_("Minimal value: 1")),
            MaxValueValidator(500, message=_("Maximal value: 500")),
        ],
    )
    total = models.DecimalField(
        default=0,
        max_digits=15,
        decimal_places=2,
        editable=False,
        verbose_name=_("Total"),
    )

    doc_prefix = "SQI"

    class Meta:
        db_table = "simpel_sales_quotation_item_bundle"
        ordering = ("position", "reg_number")
        index_together = ("item", "product")
        unique_together = ("item", "product")
        verbose_name = _("Quotation Item Bundle")
        verbose_name_plural = _("Quotation Item Bundles")
        permissions = (
            ("import_salesquotationitembundle", _("Can import Sales Quotation Item Bundle")),
            ("export_salesquotationitembundle", _("Can export Sales Quotation Item Bundle")),
        )

    def __str__(self):
        return "%s" % self.name

    def get_total(self):
        return self.price * self.quantity

    def compute(self):
        if self._state.adding and self.product is not None:
            self.name = self.product.name
            self.price = self.product.specific.total_price
        self.total = self.get_total()

    def save(self, *args, **kwargs):
        self.compute()
        return super().save(*args, **kwargs)


class SalesOrder(PolymorphicModel, NumeratorMixin, SalesOrderActionMixin, ParanoidMixin):

    # Reference & Meta Fields
    user = models.ForeignKey(
        get_user_model(),
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="sales_orders",
        verbose_name=_("Created By"),
    )
    group = models.ForeignKey(
        Group,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="salesorders",
        verbose_name=_("Group"),
    )
    customer_type = models.ForeignKey(
        ContentType,
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="salesorders",
        verbose_name=_("Customer Type"),
    )
    customer_id = models.IntegerField(
        null=True,
        blank=True,
        verbose_name=_("Customer ID"),
    )
    customer = GenericForeignKey(
        "customer_type",
        "customer_id",
    )
    reference = models.CharField(
        _("PO Number"),
        max_length=50,
        null=True,
        blank=True,
        help_text=_(
            "Purchase Order number.",
        ),
    )
    discount = models.DecimalField(
        default=0,
        max_digits=15,
        decimal_places=2,
        verbose_name=_("Discount"),
    )
    expired_at = models.DateTimeField(
        default=sales_order_expired,
        null=True,
        blank=True,
        editable=False,
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
    total = models.DecimalField(
        default=0,
        max_digits=15,
        decimal_places=2,
        editable=False,
        verbose_name=_("Total"),
    )
    grand_total = models.DecimalField(
        default=0,
        max_digits=15,
        decimal_places=2,
        editable=False,
        verbose_name=_("Grand Total"),
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

    allow_comments = models.BooleanField(default=True)

    doc_prefix = "SO"
    objects = OrderManager()

    class Meta:
        db_table = "simpel_sales_order"
        verbose_name = _("Sales Order")
        verbose_name_plural = _("Sales Orders")
        index_together = (
            "user",
            "group",
            "customer_type",
            "customer_id",
            "status",
        )
        permissions = (
            ("import_salesorder", _("Can import Sales Order")),
            ("export_salesorder", _("Can export Sales Order")),
            ("validate_salesorder", _("Can validate Sales Order")),
            ("process_salesorder", _("Can process Sales Order")),
            ("complete_salesorder", _("Can complete Sales Order")),
            ("close_salesorder", _("Can close Sales Order")),
        )

    def __str__(self):
        return "%s - %s" % (str(self.inner_id), self.customer)

    @cached_property
    def is_printable(self):
        return self.validate_ignore_condition

    @cached_property
    def is_editable(self):
        return self.is_pending

    @cached_property
    def is_invoiced(self):
        """Check object status is closed"""
        return self.invoice is not None

    @cached_property
    def is_payable(self):
        """Check object status is closed"""
        return self.is_printable and not self.is_invoiced and self.payable > 0

    @cached_property
    def has_workorder(self):
        return self.workorder is not None

    @cached_property
    def admin_url(self):
        view_name = "admin:simpel_sales_salesorder_inspect"
        return reverse(view_name, args=(self.id,), host="admin")

    def get_absolute_url(self):
        from .settings import simpel_sales_settings as sales_settings

        return reverse(sales_settings.SALESORDER_ABSOLUTE_URL_NAME, kwargs={"pk": self.pk})

    @cached_property
    def action_logs(self):
        return get_activities(self)[:5]

    @cached_property
    def billing_address(self):
        return self.addresses.filter(address_type=LinkedAddress.BILLING).first()

    @cached_property
    def shipping_address(self):
        return self.addresses.filter(address_type=LinkedAddress.SHIPPING).first()

    @cached_property
    def content_type(self):
        return ContentType.objects.get_for_model(self.__class__)

    @cached_property
    def workorder(self):
        return self.content_type.workorders.filter(reference_id=self.inner_id).first()

    @cached_property
    def qrcode(self):
        return self.qrcodes.first()

    @cached_property
    def payments(self):
        ctype = ContentType.objects.get_for_model(self.__class__)
        payments = getattr(ctype, "payments", None)
        if payments is not None:
            return payments.filter(reference_id=self.inner_id)
        return None

    @cached_property
    def invoice(self):
        invoices = getattr(self.content_type, "invoices", None)
        if invoices is None:
            return None
        invoice = self.content_type.invoices.filter(reference_id=self.inner_id).first()
        return invoice

    @cached_property
    def items_count(self):
        return self.get_items_count()

    @cached_property
    def total_items(self):
        return self.get_total_items()

    @cached_property
    def downpayment(self):
        downpayment = Decimal("0.00")
        if self.payments is not None:
            downpayment = (self.payments.filter(status__in=[const.APPROVED]).aggregate(total=models.Sum("amount")))[
                "total"
            ] or Decimal("0.00")
        return downpayment

    @cached_property
    def payable(self):
        return self.grand_total - self.downpayment

    @cached_property
    def final_document(self):
        return self.final_documents.first()

    def get_items_count(self):
        return self.items.count()

    def get_total_items(self):
        return self.items.all().aggregate(total=models.Sum("total"))["total"] or 0

    def get_grand_total(self):
        return self.total - self.discount

    def compute(self):
        self.total = self.get_total_items()
        self.grand_total = self.get_grand_total()

    def delete(self, *args, **kwargs):
        if self.qrcodes is not None:
            self.qrcodes.delete()
        if self.addresses is not None:
            self.addresses.delete()
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.compute()
        return super().save(*args, **kwargs)


class SalesOrderItem(NumeratorMixin, ParanoidMixin):
    # Reference & Meta Fields
    salesorder = models.ForeignKey(
        SalesOrder,
        related_name="items",
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        related_name="order_items",
        limit_choices_to={"is_sellable": True},
        null=False,
        blank=False,
        on_delete=models.PROTECT,
    )
    name = models.CharField(
        verbose_name=_("name"),
        max_length=255,
        null=True,
        blank=True,
        db_index=True,
    )
    alias_name = models.CharField(
        verbose_name=_("alias name"),
        max_length=255,
        null=True,
        blank=True,
        db_index=True,
    )
    note = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("Note"),
    )

    price = models.DecimalField(
        default=0,
        max_digits=15,
        decimal_places=2,
        editable=False,
        verbose_name=_("Price"),
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name=_("Quantity"),
        validators=[
            MinValueValidator(1, message=_("Minimal value: 1")),
            MaxValueValidator(500, message=_("Maximal value: 500")),
        ],
    )
    total_bundles = models.DecimalField(
        default=0,
        max_digits=15,
        decimal_places=2,
        editable=False,
        verbose_name=_("Total Bundles"),
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

    # Meta Fields
    position = models.IntegerField(
        default=0,
        verbose_name=_("position"),
        help_text=_("Enable sortable position"),
    )
    deliverable_informations = GenericRelation(
        LinkedAddress,
        content_type_field="linked_object_type",
        object_id_field="linked_object_id",
    )

    doc_prefix = "SOI"
    objects = OrderItemManager()

    class Meta:
        db_table = "simpel_sales_order_item"
        ordering = ("position", "reg_number")
        index_together = ("salesorder", "product")
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Items")
        permissions = (
            ("import_salesorderitem", _("Can import Sales Order Item")),
            ("export_salesorderitem", _("Can export Sales Order Item")),
        )

    def __str__(self):
        return "%s Order #%s" % (self.inner_id, self.salesorder.inner_id)

    @cached_property
    def deliverable_information(self):
        return self.deliverable_informations.filter(address_type=LinkedAddress.DELIVERABLE).first()

    @cached_property
    def group(self):
        return self.product.group

    @cached_property
    def group_verbose(self):
        return str(self.group)

    def get_total_bundles(self):
        return self.bundles.all().aggregate(total=models.Sum("total"))["total"] or 0

    def get_subtotal(self):
        return self.price + self.get_total_bundles()

    def get_total(self):
        return self.get_subtotal() * self.quantity

    def compute(self):
        if self._state.adding and self.product is not None:
            self.name = self.product.name
            self.price = self.product.specific.price
        self.total_bundles = self.get_total_bundles()
        self.subtotal = self.get_subtotal()
        self.total = self.get_total()

    def save(self, *args, **kwargs):
        self.compute()
        return super().save(*args, **kwargs)


class SalesOrderItemBundle(ParanoidMixin):
    # Reference & Meta Fields
    position = models.IntegerField(
        default=0,
        verbose_name=_("position"),
        help_text=_("Enable sortable position"),
    )
    item = models.ForeignKey(
        SalesOrderItem,
        related_name="bundles",
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        related_name="order_item_bundles",
        null=False,
        blank=False,
        limit_choices_to={
            "is_partial": True,
            "is_sellable": True,
        },
        on_delete=models.PROTECT,
    )
    name = models.CharField(
        verbose_name=_("name"),
        max_length=255,
        null=True,
        blank=True,
        db_index=True,
        editable=False,
    )
    price = models.DecimalField(
        default=0,
        max_digits=15,
        decimal_places=2,
        editable=False,
        verbose_name=_("Price"),
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name=_("Quantity"),
        validators=[
            MinValueValidator(1, message=_("Minimal value: 1")),
            MaxValueValidator(500, message=_("Maximal value: 500")),
        ],
    )
    total = models.DecimalField(
        default=0,
        max_digits=15,
        decimal_places=2,
        editable=False,
        verbose_name=_("Total"),
    )

    objects = OrderItemBundleManager()

    class Meta:
        db_table = "simpel_sales_order_item_bundle"
        ordering = ("position",)
        unique_together = ("item", "product")
        index_together = ("item", "product")
        verbose_name = _("Order Item Bundle")
        verbose_name_plural = _("Order Item Bundles")
        permissions = (
            ("import_salesorderitembundle", _("Can import Sales Order Item Bundle")),
            ("export_salesorderitembundle", _("Can export Sales Order Item Bundle")),
        )

    def get_total(self):
        return self.price * self.quantity

    def compute(self):
        if self._state.adding and self.product is not None:
            self.name = self.product.name
            self.price = self.product.specific.total_price
        self.total = self.get_total()

    def save(self, *args, **kwargs):
        self.compute()
        return super().save(*args, **kwargs)


class ProformaInvoice(NumeratorMixin, models.Model):

    salesorder = models.OneToOneField(
        SalesOrder,
        related_name="proforma",
        on_delete=models.CASCADE,
        verbose_name=_("Order"),
    )

    doc_prefix = "INP"

    class Meta:
        db_table = "simpel_sales_proforma_invoice"
        verbose_name = _("Proforma Invoice")
        verbose_name_plural = _("Proforma Invoices")
        permissions = (
            ("import_proformainvoice", _("Can import Proforma Invoice")),
            ("export_proformainvoice", _("Can export Proforma Invoice")),
        )

    def __str__(self):
        return self.inner_id

    @classmethod
    def get_for_order(cls, order):
        proforma, _ = cls.objects.get_or_create(order=order)
        return proforma

    @cached_property
    def admin_url(self):
        view_name = "admin:simpel_sales_proformainvoice_inspect"
        return reverse(view_name, args=(self.id,), host="admin")
