from simpel.simpel_products.resources import ProductResourceBase, product_fields

from .models import ConsultancyService


class ConsultancyServiceResource(ProductResourceBase):
    class Meta:
        model = ConsultancyService
        fields = product_fields + ["price"]
        export_order = product_fields + ["price"]
        import_id_fields = ("inner_id",)
