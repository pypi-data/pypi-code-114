
from django.db import models
from django.utils.translation import gettext_lazy as _

from simpel.simpel_core.abstracts import ParanoidMixin
from simpel.simpel_products.models import Bundle, Group
from simpel.simpel_projects.models import Task  # NOQA
from simpellab.mod_base.models import AnalysisMethod, Parameter  # NOQA


class InspectionService(Bundle):

    help_text = _(
        "This is ispection service, adding or removing parameter is allowed,"
        " and pricing can dynamically changed based on chosen parameters."
    )
    
    doc_prefix = "LIT"
    has_parameters = True

    class Meta:
        db_table = "simpel_inspection_service"
        verbose_name = _("Inspection Service")
        verbose_name_plural = _("Inspection Services")
        permissions = (
            ("export_inspectionservice", _("Can export Inspection Service")),
            ("import_inspectionservice", _("Can import Inspection Service")),
        )

    def save(self, *args, **kwargs):
        self.is_bundle = True
        self.is_partial = False
        self.is_sellable = True
        if self.group is None:
            self.group = Group.get_or_create("LIT", "Inspection")
        if self.is_deliverable is None:
            self.is_deliverable = True
        return super().save(*args, **kwargs)


class InspectionTask(Task):
    # Reference & Meta Fields

    doc_prefix = "TSK.LIT"

    class Meta:
        db_table = "simpel_inspection_task"
        ordering = ("position",)
        verbose_name = _("Inspection Task")
        verbose_name_plural = _("Inspection Tasks")
        permissions = (
            ("import_inspectiontask", _("Can import Inspection Task")),
            ("export_inspectiontask", _("Can export Inspection Task")),
        )


class InspectionTaskParameter(ParanoidMixin):
    # Reference & Meta Fields
    position = models.IntegerField(default=0, verbose_name=_("position"), help_text=_("Enable sortable position"))
    task = models.ForeignKey(
        InspectionTask,
        related_name="parameters",
        on_delete=models.CASCADE,
    )
    parameter = models.ForeignKey(
        Parameter,
        related_name="inspection_task_parameters",
        null=False,
        blank=False,
        on_delete=models.PROTECT,
    )
    analysis_method = models.ForeignKey(
        AnalysisMethod,
        related_name="inspection_task_parameters",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
    )

    class Meta:
        db_table = "simpel_inspection_task_parameter"
        ordering = ("position",)
        unique_together = ("task", "parameter")
        verbose_name = _("Inspection Task Parameter")
        verbose_name_plural = _("Inspection Task Parameters")
        permissions = (
            ("import_inspectiontaskparameter", _("Can import Inspection Task Parameter")),
            ("export_inspectiontaskparameter", _("Can export Inspection Task Parameter")),
        )
