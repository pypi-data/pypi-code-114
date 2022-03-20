from django.db import models
from django.utils.translation import gettext_lazy as _
from simpel.simpel_products.models import Product
from simpel.utils import unique_slugify

LEN_SHORT = 128
LEN_LONG = 256


class ProductGroup(models.TextChoices):
    LABORATORIUM = "LAB", _("Laboratorium")
    INSPECTION = "LIT", _("Technical Inspection")
    CALIBRATION = "KAL", _("Calibration")
    CERTIFICATION = "PRO", _("Product Certification")
    CONSULTANCY = "KSL", _("Consultancy")
    RESEARCH = "LIB", _("Research and Development")
    TRAINING = "LAT", _("Training")
    SERVICE = "SRV", _("Service")
    PARAMETER = "PRM", _("Parameter")
    FEE = "FEE", _("Fee")


class AnalysisMethod(models.Model):

    name = models.CharField(
        max_length=128,
        verbose_name=_("test method"),
    )
    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True,
        editable=False,
        max_length=80,
    )
    description = models.TextField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_("Description"),
    )
    reference = models.URLField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_("reference"),
    )

    icon = "microscope"

    class Meta:
        db_table = "simpel_analysis_method"
        verbose_name = _("Analisys Method")
        verbose_name_plural = _("Analisys Methods")
        permissions = (
            ("import_analysismethod", _("Can import Analisys Method")),
            ("export_analysismethod", _("Can export Analisys Method")),
        )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            unique_slugify(self, self.name)
        return super().save(*args, **kwargs)


class Parameter(Product):

    unit_code = models.CharField(
        null=True,
        blank=True,
        max_length=122,
        verbose_name=_("Unit Code"),
    )
    analysis_method = models.ForeignKey(
        AnalysisMethod,
        related_name="parameters",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
    )
    doc_prefix = "PRM"

    def save(self, *args, **kwargs):
        self.is_partial = True
        self.is_deliverable = False
        self.is_sellable = True
        return super().save(*args, **kwargs)

    class Meta:
        db_table = "simpel_parameter"
        verbose_name = _("Parameter")
        verbose_name_plural = _("Parameters")
        permissions = (
            ("export_parameter", _("Can export Parameter")),
            ("import_parameter", _("Can import Parameter")),
        )


class ParameterMethod(models.Model):

    parameter = models.ForeignKey(
        Parameter,
        related_name="analysis_methods",
        on_delete=models.PROTECT,
    )
    method = models.ForeignKey(
        AnalysisMethod,
        related_name="parameter_methods",
        on_delete=models.PROTECT,
    )
    min_quality_value = models.CharField(
        max_length=128,
        verbose_name=_("min quality value"),
    )
    max_quality_value = models.CharField(
        max_length=128,
        verbose_name=_("max quality value"),
    )

    class Meta:
        db_table = "simpel_parameter_method"
        verbose_name = _("Parameter Method")
        verbose_name_plural = _("Parameter Method")
        permissions = (
            ("export_parametermethod", _("Can export Parameter Method")),
            ("import_parametermethod", _("Can import Parameter Method")),
        )
