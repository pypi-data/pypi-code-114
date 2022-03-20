from decimal import Decimal

from django.contrib.admin.templatetags.admin_urls import admin_urlname
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.forms import ValidationError
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _
from polymorphic.models import PolymorphicModel

from simpel.simpel_auth.models import LinkedAddress
from simpel.simpel_auth.utils import get_activities
from simpel.simpel_core import const
from simpel.simpel_core.models import CustomGenericForeignKey, NumeratorMixin
from simpel.simpel_core.models.models import BaseSetting
from simpel.simpel_core.models.registries import register_setting
from simpel.simpel_core.models.templates import PathModelTemplate
from simpel.simpel_products.models import Group
from simpel.simpel_sales.models import SalesOrder
from simpel.utils import reverse

from .mixins import WorkOrderActionMixin


@register_setting
class ProjectsSetting(BaseSetting):
    invoice_template = models.ForeignKey(
        PathModelTemplate,
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.SET_NULL,
        verbose_name=_("Work Order Template"),
        help_text=_("Custom Work Order template."),
    )


class WorkOrder(PolymorphicModel, WorkOrderActionMixin, NumeratorMixin):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        related_name="workorders",
        verbose_name=_("user"),
        null=True,
        blank=True,
        editable=False,
    )
    group = models.ForeignKey(
        Group,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="workorders",
        verbose_name=_("Group"),
    )
    customer_type = models.ForeignKey(
        ContentType,
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="workorder_customers",
        verbose_name=_("Customer Type"),
    )
    customer_id = models.IntegerField(null=True, blank=True, verbose_name=_("Customer ID"))

    customer = GenericForeignKey("customer_type", "customer_id")
    reference_type = models.ForeignKey(
        ContentType,
        limit_choices_to={"model__in": ["salesorder"]},
        null=True,
        blank=False,
        related_name="workorders",
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
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    content = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("Content"),
    )
    data = models.JSONField(
        null=True,
        blank=True,
        verbose_name=_("Data"),
        help_text=_("Extra data in JSON format."),
    )

    addresses = GenericRelation(
        LinkedAddress,
        content_type_field="linked_object_type",
        object_id_field="linked_object_id",
    )

    autoprocess = models.BooleanField(
        default=True,
        null=True,
        blank=True,
        verbose_name=_("Auto Process"),
        help_text=_("Auto proccess reference when work order validated."),
    )
    autoclose = models.BooleanField(
        default=True,
        null=True,
        blank=True,
        verbose_name=_("Auto Close"),
        help_text=_("Auto close reference whene all task done."),
    )
    progress = models.DecimalField(
        default=0.00,
        decimal_places=2,
        max_digits=5,
        verbose_name=_("Progress"),
        editable=False,
    )
    icon = "text-box-outline"

    doc_prefix = "WO"

    class Meta:
        db_table = "simpel_project_workorder"
        verbose_name = _("Work Order")
        verbose_name_plural = _("Work Orders")
        permissions = (
            ("import_workorder", _("Can import Work Order")),
            ("export_workorder", _("Can export Work Order")),
            ("validate_workorder", _("Can validate Work Order")),
            ("process_workorder", _("Can process Work Order")),
            ("complete_workorder", _("Can complete Work Order")),
        )

    def __str__(self):
        return self.inner_id

    def clean(self):
        if self.reference_type is not None and self.reference is None:
            raise ValidationError({"reference_id": _("Reference not found.")})
        if self.reference:
            if self.reference.status not in [const.VALID]:
                raise ValidationError(
                    {
                        "reference_id": _("Reference status is not Valid. [%s]") % self.reference.get_status_display(),
                    }
                )

    @cached_property
    def opts(self):
        return self.get_real_instance_class()._meta

    @cached_property
    def specific(self):
        return self.get_real_instance()

    @cached_property
    def action_logs(self):
        return get_activities(self)[:5]

    @cached_property
    def admin_url(self):
        return reverse(admin_urlname(self.__class__._meta, "inspect"), args=(self.id,))

    @cached_property
    def progress_complete(self):
        progress = self.get_progress()
        return progress >= 100

    def get_progress(self):
        items = [item.progress for item in self.items.all()]
        if len(items) <= 0:
            return Decimal(0.00)
        return round(sum(items) / len(items), 2)

    def save(self, *args, **kwargs):
        self.progress = self.get_progress()
        return super().save(*args, **kwargs)


class Task(PolymorphicModel, NumeratorMixin):
    position = models.IntegerField(
        default=0,
        verbose_name=_("position"),
        help_text=_("Enable sortable position"),
    )
    workorder = models.ForeignKey(
        WorkOrder,
        related_name="items",
        on_delete=models.CASCADE,
    )
    start_at = models.DateField(
        default=timezone.now,
        verbose_name=_("Start"),
    )
    end_at = models.DateField(
        default=timezone.now,
        verbose_name=_("End"),
    )
    name = models.CharField(
        verbose_name=_("name"),
        max_length=255,
        null=True,
        blank=True,
        db_index=True,
    )
    reference_type = models.ForeignKey(
        ContentType,
        limit_choices_to={"model__in": ["salesorderitem"]},
        null=True,
        blank=False,
        related_name="tasks",
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
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name=_("Quantity"),
    )
    note = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("Note"),
    )

    deliverable_informations = GenericRelation(
        LinkedAddress,
        content_type_field="linked_object_type",
        object_id_field="linked_object_id",
    )

    doc_prefix = "TSK"

    class Meta:
        db_table = "simpel_project_task"
        ordering = ("position",)
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")
        permissions = (
            ("import_task", _("Can import Task")),
            ("export_task", _("Can export Tasks")),
            ("export_complete", _("Can complete Tasks")),
        )

    @cached_property
    def base_opts(self):
        return Task._meta

    @cached_property
    def opts(self):
        return self.get_real_instance_class()._meta

    @cached_property
    def specific(self):
        return self.get_real_instance()

    def clean(self):
        if self.reference_type is not None and self.reference is None:
            raise ValidationError({"reference_id": _("Reference not found.")})

    def get_parameters(self):
        # TODO sementara, ambil parameter untuk cetak workorder
        return [
            item.product.specific
            for item in self.reference.bundles.all()
            if item.product.specific.opts.model_name == "parameter"
        ]

    @cached_property
    def deliverable_information(self):
        return self.deliverable_informations.filter(address_type=LinkedAddress.DELIVERABLE).first()

    @cached_property
    def completes(self):
        return self.deliverables.count()

    @cached_property
    def progress(self):
        pg = (self.completes / self.quantity) * 100
        return round(pg, 2)

    @cached_property
    def progress_complete(self):
        return self.completes >= self.quantity

    def __str__(self):
        return "%s WO #%s" % (self.inner_id, self.workorder.inner_id)


class Deliverable(NumeratorMixin, PolymorphicModel):
    issued_date = models.DateTimeField(
        default=timezone.now,
        verbose_name=_("Issued date"),
    )
    customer_type = models.ForeignKey(
        ContentType,
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="deliverable_customers",
        verbose_name=_("Customer Type"),
    )
    customer_id = models.IntegerField(null=True, blank=True, verbose_name=_("Customer ID"))

    customer = GenericForeignKey("customer_type", "customer_id")
    task = models.ForeignKey(
        Task,
        null=True,
        blank=False,
        limit_choices_to={"workorder__status": WorkOrder.VALID},
        related_name="deliverables",
        on_delete=models.SET_NULL,
        verbose_name=_("Task"),
    )
    template = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        editable=False,
        verbose_name=_("Deliverable Template"),
    )
    attachment = models.FileField(
        null=True,
        blank=True,
        verbose_name=_("attachment"),
    )

    live = models.BooleanField(default=False)

    icon = "certificate-outline"

    class Meta:
        db_table = "simpel_project_deliverable"
        verbose_name = _("Deliverable")
        verbose_name_plural = _("Deliverables")
        permissions = (
            ("import_deliverable", _("Can import Deliverable")),
            ("export_deliverable", _("Can export Deliverable")),
        )

    def __str__(self):
        return "%s %s" % (self.opts.verbose_name, self.inner_id)

    @cached_property
    def base_opts(self):
        return Deliverable._meta

    @cached_property
    def opts(self):
        return self.get_real_instance_class()._meta

    @cached_property
    def specific(self):
        return self.get_real_instance()

    def compute(self):
        self.customer = self.task.workorder.customer

    def get_template_name(self):
        template_name = self.template or self.template_name
        return template_name

    def clean(self):
        if self.task.progress_complete:
            raise ValidationError(_("This task has been complete."))

    def save(self, *args, **kwargs):
        self.compute()
        return super().save(*args, **kwargs)


class CancelationDeliverable(Deliverable):
    reason = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_("Cancelation reason"),
    )
    doc_prefix = "CND"

    formset_fields = ["issued_date", "reason", "attachment", "live"]

    class Meta:
        db_table = "simpel_project_cancelation_note"
        verbose_name = _("Cancelation Note")
        verbose_name_plural = _("Cancelation Notes")
        permissions = (
            ("import_cancelationdeliverable", _("Can import Cancelation Note")),
            ("export_cancelationdeliverable", _("Can export Cancelation Note")),
        )


class DocumentDeliverable(Deliverable):
    addresses = GenericRelation(
        LinkedAddress,
        content_type_field="linked_object_type",
        object_id_field="linked_object_id",
    )

    doc_prefix = "CRT"
    formset_fields = ["issued_date", "attachment", "live"]

    def compute(self):
        self.customer = self.task.workorder.customer
        del_info = getattr(self.task.reference, "deliverable_information", None)
        if del_info:
            data = del_info.to_dict()
        else:
            data = self.task.workorder.customer.get_deliverable_info()
        for key, val in data.items():
            setattr(self, key, val)

    class Meta:
        db_table = "simpel_project_deliverable_document"
        verbose_name = _("Document Deliverable")
        verbose_name_plural = _("Document Deliverables")
        permissions = (
            ("import_documentdeliverable", _("Can import Document Deliverable")),
            ("export_documentdeliverable", _("Can export Document Deliverable")),
        )


class FinalDocument(NumeratorMixin, PolymorphicModel):
    PROCESSED = const.PROCESSED
    COMPLETE = const.COMPLETE
    STATUS_CHOICES = (
        (const.PROCESSED, _("Processed")),
        (const.COMPLETE, _("Complete")),
    )

    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=const.PROCESSED,
    )
    user = models.ForeignKey(
        get_user_model(),
        null=True,
        blank=True,
        related_name="final_documents",
        on_delete=models.SET_NULL,
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        null=True,
        blank=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        default=timezone.now,
        null=True,
        blank=True,
        editable=False,
    )
    workorder = models.OneToOneField(
        WorkOrder,
        related_name="final_document",
        on_delete=models.CASCADE,
        limit_choices_to={
            "status__in": [
                SalesOrder.VALID,
                SalesOrder.PROCESSED,
                SalesOrder.COMPLETE,
            ],
        },
        verbose_name=_("Sales Order"),
    )

    doc_prefix = "FDI"
    parent_prefix = True

    class Meta:
        db_table = "simpel_project_final_document"
        verbose_name = _("Final Document")
        verbose_name_plural = _("Final Documents")
        permissions = (
            ("import_finaldocument", _("Can import Final Document")),
            ("export_finaldocument", _("Can export Final Document")),
        )

    @cached_property
    def parent_model(self):
        return FinalDocument._meta.model_name

    @cached_property
    def opts(self):
        return self.__class__._meta

    @cached_property
    def specific(self):
        return self.get_real_instance()

    def __str__(self):
        return "%s (%s)" % (self.inner_id, self.work_order)


class FinalDocumentItem(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        null=True,
        blank=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        default=timezone.now,
        null=True,
        blank=True,
        editable=False,
    )
    final_document = models.ForeignKey(
        FinalDocument,
        related_name="items",
        on_delete=models.CASCADE,
        verbose_name=_("Final Document"),
    )
    deliverable = models.OneToOneField(
        Deliverable,
        null=True,
        blank=True,
        related_name="finaldocument_items",
        on_delete=models.CASCADE,
        verbose_name=_("Deliverable"),
    )
    reference = models.CharField(
        max_length=255,
        verbose_name=_("Deliverable Number"),
    )
    note = models.CharField(
        _("Note"),
        max_length=255,
        null=True,
        blank=True,
    )

    def __str__(self):
        return "%s" % (self.reference)

    class Meta:
        db_table = "simpel_project_final_document_item"
        verbose_name = _("Final Document Item")
        verbose_name_plural = _("Final Document Items")
        permissions = (
            ("import_finaldocumentitem", _("Can import Final Document Item")),
            ("export_finaldocumentitem", _("Can export Final Document Item")),
        )


class FinalDocumentRegistry(NumeratorMixin):
    final_document = models.ForeignKey(
        FinalDocument,
        related_name="registers",
        on_delete=models.CASCADE,
    )

    doc_prefix = "FDR"

    class Meta:
        db_table = "simpel_project_final_document_registry"
        verbose_name = _("Final Document Registry")
        verbose_name_plural = _("Final Document Registries")
        permissions = (
            ("import_finaldocumentregistry", _("Can import Final Document Registry")),
            ("export_finaldocumentregistry", _("Can export Final Document Registries")),
        )

    def __str__(self):
        return super().__str__()
