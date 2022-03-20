from import_export.resources import ModelResource

from .models import Invoice

INV_FIELDS = [
    "created_at",
    "issued_date",
    "due_date",
    "inner_id",
    "customer",
    "reference_id",
    "items_count",
    "total",
    "discount",
    "downpayment",
    "grand_total",
    "paid",
    "payable",
    "refund",
]


class InvoiceResource(ModelResource):
    class Meta:
        model = Invoice
        fields = INV_FIELDS
        export_order = INV_FIELDS
        import_id_fields = ("inner_id",)
