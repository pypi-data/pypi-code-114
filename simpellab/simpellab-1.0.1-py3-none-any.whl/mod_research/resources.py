from simpel.simpel_products.resources import ProductResourceBase, product_fields

from .models import ResearchService


class ResearchServiceResource(ProductResourceBase):
    class Meta:
        model = ResearchService
        fields = product_fields + ["price"]
        export_order = product_fields + ["price"]
        import_id_fields = ("inner_id",)
