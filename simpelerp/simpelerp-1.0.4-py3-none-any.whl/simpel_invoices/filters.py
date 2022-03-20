from django.utils.translation import gettext_lazy as _
from django_filters import filters
from django_filters.filterset import FilterSet

from simpel.simpel_products.models import Group

from .models import Invoice


class InvoiceFilterSet(FilterSet):
    status = filters.MultipleChoiceFilter(
        choices=Invoice.STATUS_CHOICES,
        field_name="status",
        label=_("Status"),
    )
    group = filters.ModelMultipleChoiceFilter(
        queryset=Group.objects.filter(
            code__in=[
                "KAL",
                "LAB",
                "LIT",
                "LAT",
                "PRO",
                "LIB",
                "KSL",
            ]
        )
    )

    class Meta:
        model = Invoice
        fields = ("status", "group")
