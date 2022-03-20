from django.db import models
from django.utils.translation import gettext_lazy as _

from simpel.simpel_core.abstracts import ParanoidMixin
from simpel.simpel_products.models import Bundle, Group
from simpel.simpel_projects.models import Task  # NOQA
from simpellab.mod_base.models import AnalysisMethod, Parameter

LEN_SHORT = 128
LEN_LONG = 256


class LaboratoriumService(Bundle):

    doc_prefix = "LAB"
    has_parameters = True

    class Meta:
        db_table = "simpel_laboratorium_service"
        verbose_name = _("Laboratorium Service")
        verbose_name_plural = _("Laboratorium Services")
        permissions = (
            ("export_laboratoriumservice", _("Can export Laboratorium Service")),
            ("import_laboratoriumservice", _("Can import Laboratorium Service")),
        )

    def save(self, *args, **kwargs):
        self.is_bundle = True
        self.is_partial = False
        self.is_sellable = True
        if self.group is None:
            self.group = Group.get_or_create("LAB", "Laboratorium")
        if self.is_deliverable is None:
            self.is_deliverable = True
        return super().save(*args, **kwargs)


class LaboratoriumTask(Task):
    # Reference & Meta Fields

    doc_prefix = "TSK.LAB"

    class Meta:
        db_table = "simpel_laboratorium_task"
        ordering = ("position",)
        verbose_name = _("Laboratorium Task")
        verbose_name_plural = _("Laboratorium Tasks")
        permissions = (
            ("import_laboratoriumtask", _("Can import Laboratorium Task")),
            ("export_laboratoriumtask", _("Can export Laboratorium Task")),
        )


class LaboratoriumTaskParameter(ParanoidMixin):
    # Reference & Meta Fields
    position = models.IntegerField(
        default=0,
        verbose_name=_("position"),
        help_text=_("Enable sortable position"),
    )
    task = models.ForeignKey(
        LaboratoriumTask,
        related_name="parameters",
        on_delete=models.CASCADE,
    )
    parameter = models.ForeignKey(
        Parameter,
        related_name="laboratorium_task_parameters",
        null=False,
        blank=False,
        on_delete=models.PROTECT,
    )
    analysis_method = models.ForeignKey(
        AnalysisMethod,
        related_name="laboratorium_task_parameters",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
    )

    class Meta:
        db_table = "simpel_laboratorium_task_parameter"
        ordering = ("position",)
        unique_together = ("task", "parameter")
        verbose_name = _("Laboratorium Task Parameter")
        verbose_name_plural = _("Laboratorium Task Parameters")
        permissions = (
            ("import_laboratoriumtaskparameter", _("Can import Laboratorium Task Parameter")),
            ("export_laboratoriumtaskparameter", _("Can export Laboratorium Task Parameter")),
        )
