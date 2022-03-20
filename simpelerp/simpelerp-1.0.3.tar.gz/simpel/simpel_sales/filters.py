from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django_filters import filters
from django_filters.filterset import FilterSet

# TODO maybe unused
from simpel.simpel_products.filters import get_product_child_choices
from simpel.simpel_products.models import Group

from .models import SalesOrder, SalesQuotation


class SalesOrderFilterSet(FilterSet):
    status = filters.MultipleChoiceFilter(
        choices=SalesOrder.STATUS_CHOICES,
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
        model = SalesOrder
        fields = ("status", "group")


class SalesQuotationFilterSet(FilterSet):
    status = filters.MultipleChoiceFilter(
        choices=SalesQuotation.STATUS_CHOICES,
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
        model = SalesOrder
        fields = ("status", "group")


class OrderAdminFilterSet(admin.SimpleListFilter):
    """Django Admin Product Filter by Polymorphic Type"""

    title = _("Service Type")
    parameter_name = "contenttype_id"

    def lookups(self, request, model_admin):
        return get_product_child_choices(key_name="id")

    def queryset(self, request, queryset):
        if not self.value():
            return queryset

        return queryset.filter(contenttype_id=self.value())
