from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class ReportLog(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        related_name=_("report_logs"),
        on_delete=models.CASCADE,
        db_index=True,
    )
    created_at = models.DateTimeField(
        default=timezone.now,
    )
    dataname = models.CharField(
        max_length=255,
    )
    file = models.FileField(
        verbose_name=_("File"),
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "simpel_report_log"
        verbose_name = _("Report Log")
        verbose_name_plural = _("Report Logs")
