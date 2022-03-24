from import_export.resources import ModelResource

from .models import Partner

partner_fields = [
    "id",
    "created_at",
    "reg_number",
    "inner_id",
    "partner_type",
    "user",
    "doc",
    "idn",
    "tax_id",
    "name",
    "text",
    "html",
    "is_active",
    "is_verified",
    "is_customer",
    "is_supplier",
]


class PartnerResource(ModelResource):
    class Meta:
        model = Partner
        fields = partner_fields
        export_order = partner_fields
        import_id_fields = ("inner_id",)
