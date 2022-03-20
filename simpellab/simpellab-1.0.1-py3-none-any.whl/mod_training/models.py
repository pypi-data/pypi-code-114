from django.db import models
from django.utils.translation import gettext_lazy as _

from simpel.simpel_products.models import Group, Product


class TrainingService(Product):

    audience_criterias = models.TextField(
        verbose_name=_("Audience criterias"),
    )

    doc_prefix = "LAT"

    class Meta:
        db_table = "simpel_training_service"
        verbose_name = _("Training and Coaching")
        verbose_name_plural = _("Training and Coachings")
        permissions = (
            ("export_trainingservice", _("Can export Training Service")),
            ("import_trainingservice", _("Can import Training Service")),
        )

    def get_doc_prefix(self):
        return "LAT"

    def save(self, *args, **kwargs):
        self.is_partial = False
        self.is_sellable = True
        if self.group is None:
            self.group = Group.get_or_create("LAT", "Training")
        if self.is_deliverable is None:
            self.is_deliverable = True
        return super().save(*args, **kwargs)


class TrainingTopic(models.Model):
    service = models.ForeignKey(
        TrainingService,
        related_name="topics",
        on_delete=models.CASCADE,
        verbose_name=_("Service"),
    )
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        db_table = "simpel_product_training_topic"
        verbose_name = _("Training Topic")
        verbose_name_plural = _("Training Topics")
        permissions = (
            ("export_trainingtopic", _("Can export Training Topic")),
            ("import_trainingtopic", _("Can import Training Topic")),
        )

    def __str__(self):
        return str(self.title)
