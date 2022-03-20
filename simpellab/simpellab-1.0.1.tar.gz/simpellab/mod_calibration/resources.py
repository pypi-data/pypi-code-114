from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget

from simpel.simpel_products.resources import ProductResourceBase, product_fields
from simpellab.mod_base.models import AnalysisMethod

from .models import CalibrationService


class CalibrationServiceResource(ProductResourceBase):
    analysis_method = Field(
        attribute="analysis_method",
        column_name="analysis_method",
        widget=ForeignKeyWidget(AnalysisMethod, field="slug"),
    )

    class Meta:
        model = CalibrationService
        fields = product_fields + ["analysis_method", "price"]
        export_order = product_fields + ["analysis_method", "price"]
        import_id_fields = ("inner_id",)
