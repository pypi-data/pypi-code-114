from import_export.resources import ModelResource

from .models import SalesOrder, SalesQuotation

SO_FIELDS = (
    "inner_id",
    "group",
    "customer",
    "created_at",
    "total",
    "discount",
    "grand_total",
)


class SalesOrderResource(ModelResource):
    class Meta:
        model = SalesOrder
        fields = SO_FIELDS
        export_order = SO_FIELDS
        import_id_fields = ("inner_id",)


SQ_FIELDS = (
    "inner_id",
    "group",
    "customer",
    "created_at",
    "expired_at",
    "sampling",
    "scheduled_at",
    "total",
    "grand_total",
)


class SalesQuotationResource(ModelResource):
    class Meta:
        model = SalesQuotation
        fields = SQ_FIELDS
        export_order = SQ_FIELDS
        import_id_fields = ("inner_id",)
