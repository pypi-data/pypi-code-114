from import_export.fields import Field
from import_export.resources import ModelResource
from import_export.widgets import ForeignKeyWidget

from simpel.simpel_products.resources import ProductResourceBase, product_fields

from .models import AnalysisMethod, Parameter


class AnalysisMethodResource(ModelResource):
    class Meta:
        model = AnalysisMethod


class ParameterResource(ProductResourceBase):
    analysis_method = Field(
        attribute="analysis_method",
        column_name="analysis_method",
        widget=ForeignKeyWidget(AnalysisMethod, field="slug"),
    )

    class Meta:
        model = Parameter
        fields = product_fields + ["analysis_method", "unit_code", "price"]
        export_order = product_fields + ["analysis_method", "unit_code", "price"]
        import_id_fields = ("inner_id",)
