from simpel.simpel_products.resources import ProductResourceBase, product_fields

from .models import CertificationService


class CertificationServiceResource(ProductResourceBase):
    class Meta:
        model = CertificationService
        fields = product_fields + ["price"]
        export_order = product_fields + ["price"]
        import_id_fields = ("inner_id",)
