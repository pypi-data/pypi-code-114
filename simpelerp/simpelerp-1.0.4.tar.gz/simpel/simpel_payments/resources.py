from django.contrib.contenttypes.models import ContentType
from import_export.fields import Field
from import_export.resources import ModelResource
from import_export.widgets import ForeignKeyWidget

from .models import Payment, PaymentGateway

payment_fields = [
    "user",
    "status",
    "reference_type",
    "reference_id",
    "source_type",
    "source_id",
    "destination_type",
    "destination_id",
    "amount",
    "note",
    "created_at",
    "confirmed_at",
    "rejected_at",
    "refunded_at",
]


class PaymentResource(ModelResource):
    reference_type = Field(
        attribute="reference_type",
        column_name="reference_type",
        widget=ForeignKeyWidget(ContentType, field="model"),
    )
    gateway = Field(
        attribute="gateway",
        column_name="gateway",
        widget=ForeignKeyWidget(PaymentGateway, field="model"),
    )

    class Meta:
        model = Payment
        fields = payment_fields
        export_order = payment_fields
        import_id_fields = ("inner_id",)


# class WithdrawResource(ModelResource):
#     source = Field(
#         attribute="source",
#         column_name="source",
#         widget=ForeignKeyWidget(PaymentGateway, field="name"),
#     )
#     destination = Field(
#         attribute="destination",
#         column_name="destination",
#         widget=ForeignKeyWidget(Partner, field="inner_id"),
#     )

#     class Meta:
#         model = Withdraw
#         fields = payment_fields
#         export_order = payment_fields
#         import_id_fields = ("inner_id",)
