from django.db import models
from django.utils.translation import gettext_lazy as _

from simpel.simpel_products.models import Group, Product
from simpel.simpel_projects.models import Task
from simpellab.mod_base.models import AnalysisMethod


class CalibrationService(Product):
    
    analysis_method = models.ForeignKey(
        AnalysisMethod,
        related_name="calibrations",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
    )

    doc_prefix = "KAL"

    class Meta:
        db_table = "simpel_calibration_service"
        verbose_name = _("Calibration Service")
        verbose_name_plural = _("Calibration Services")
        permissions = (
            ("export_calibrationservice", _("Can export Calibration Service")),
            ("import_calibrationservice", _("Can import Calibration Service")),
        )

    def get_doc_prefix(self):
        return "KAL"

    def save(self, *args, **kwargs):
        if self.is_partial is None:
            self.is_partial = False
        if self.is_deliverable is None:
            self.is_deliverable = True
        self.is_sellable = True
        if self.group is None:
            self.group = Group.get_or_create("KAL", "Calibration")
        return super().save(*args, **kwargs)


class CalibrationTask(Task):
    class Meta:
        db_table = "simpel_calibration_task"
        verbose_name = _("Calibration Task")
        verbose_name_plural = _("Calibration Task")
