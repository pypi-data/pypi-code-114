from simpel.simpel_products.resources import ProductResourceBase, product_fields

from .models import InspectionService


class InspectionServiceResource(ProductResourceBase):
    class Meta:
        model = InspectionService
        fields = product_fields
        export_order = product_fields
        import_id_fields = ("inner_id",)
