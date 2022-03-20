from simpel.simpel_products.resources import ProductResourceBase, product_fields

from .models import LaboratoriumService


class LaboratoriumServiceResource(ProductResourceBase):
    class Meta:
        model = LaboratoriumService
        fields = product_fields + ["price"]
        export_order = product_fields + ["price"]
        import_id_fields = ("inner_id",)
