from django.contrib import admin
from django.forms.widgets import SelectMultiple
from django.utils.translation import gettext_lazy as _
from django_filters.filters import CharFilter, MultipleChoiceFilter
from django_filters.filterset import FilterSet

from simpel.simpel_products.filters import get_product_child_choices
from simpel.simpel_shop.models import CartItem


class CartFilterSet(FilterSet):
    name = CharFilter(
        field_name="name",
        lookup_expr="icontains",
        label=_("Search by Name"),
    )

    class Meta:
        model = CartItem
        fields = ("name",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters["product_type"] = MultipleChoiceFilter(
            label=_("Product Types"),
            field_name="product__polymorphic_ctype",
            widget=SelectMultiple(),
            choices=get_product_child_choices(key_name="id"),
            help_text=_("Press CTRL + Click to select the choices."),
        )


class CartAdminFilterSet(admin.SimpleListFilter):
    """Django Admin Product Filter by Polymorphic Type"""

    title = _("Product Type")
    parameter_name = "product__ctype"

    def lookups(self, request, model_admin):
        return get_product_child_choices()

    def queryset(self, request, queryset):
        if not self.value():
            return queryset

        return queryset.filter(product__polymorphic_ctype=self.value())
