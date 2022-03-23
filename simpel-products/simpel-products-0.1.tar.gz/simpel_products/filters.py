from django.conf import settings
from django.contrib import admin
from django.core.cache import cache
from django.forms import CheckboxSelectMultiple
from django.utils.translation import ugettext_lazy as _

from django_filters import filters
from django_filters.filterset import FilterSet
from simpel_admin.filters import PreFilteredListFilter
from simpel_hookup import core as hookup
from simpel_utils.contenttypes import get_polymorpohic_choice

from .models import Group, Product


def get_product_child_choices(key_name="id", separator=".", sort_value=False):
    # Generate cache key
    cache_key_name = key_name
    if isinstance(key_name, (list, tuple, set)):
        cache_key_name = separator.join([str(key) for key in key_name])
    cache_key = "ProductChildChoiches:%s" % str(cache_key_name)
    cache_timeout = 60 * 60 * 24
    if settings.DEBUG:
        cache_timeout = 60
    # Get choices from cache
    choices = cache.get(cache_key)
    if not choices:
        funcs = hookup.get_hooks("REGISTER_PRODUCT_CHILD_MODELS")
        models = [func() for func in funcs]
        choices = get_polymorpohic_choice(models, key_name=key_name, separator=separator, sort_value=sort_value)
        cache.set(cache_key, choices, cache_timeout)
    return choices


class ProductAdminFilterSet(admin.SimpleListFilter):
    """Django Admin Product Filter by Polymorphic Type"""

    title = _("Product by Type")
    parameter_name = "ctype"

    def lookups(self, request, model_admin):
        return get_product_child_choices()

    def queryset(self, request, queryset):
        if not self.value():
            return queryset

        return queryset.filter(polymorphic_ctype=self.value())


class AdminBundleFilter(PreFilteredListFilter):
    default_value = False
    title = _("Partial")
    parameter_name = "bundle"

    def queryset(self, request, queryset):
        if not self.value():
            return queryset.filter(bundle=self.get_default_value())
        return queryset.filter(bundle=self.value())

    def lookups(self, request, model_admin):
        return ((True, _("Yes")), (False, _("No")))


class ProductFilterSet(FilterSet):
    name = filters.CharFilter(
        field_name="name",
        lookup_expr="icontains",
        label=_("Search by Name"),
    )
    group = filters.ModelMultipleChoiceFilter(
        label=_("Groups"),
        queryset=Group.objects.all(),
        widget=CheckboxSelectMultiple(),
        help_text=_("Click to select the choices."),
    )

    class Meta:
        model = Product
        fields = ("name", "group")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters["product_type"] = filters.MultipleChoiceFilter(
            label=_("Product Types"),
            field_name="polymorphic_ctype",
            widget=CheckboxSelectMultiple(),
            choices=get_product_child_choices(key_name="id"),
            help_text=_("Click to select the choices."),
        )
