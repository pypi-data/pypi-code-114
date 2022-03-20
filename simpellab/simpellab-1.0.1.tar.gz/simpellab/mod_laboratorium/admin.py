import nested_admin
from django.contrib import admin
from django.contrib.admin.widgets import AdminTextareaWidget

from simpel.simpel_products.admin import BundleAdmin

from .models import LaboratoriumService, LaboratoriumTask, LaboratoriumTaskParameter
from .resources import LaboratoriumServiceResource


@admin.register(LaboratoriumService)
class LaboratoriumServiceAdmin(BundleAdmin):
    resource_class = LaboratoriumServiceResource


class LaboratoriumTaskParameterInline(
    nested_admin.SortableHiddenMixin,
    nested_admin.NestedTabularInline,
):
    model = LaboratoriumTaskParameter
    extra = 0
    autocomplete_fields = ["parameter", "analysis_method"]


class LaboratoriumTaskInline(
    nested_admin.SortableHiddenMixin,
    nested_admin.NestedStackedInline,
):
    model = LaboratoriumTask
    widgets = {"note": AdminTextareaWidget(attrs={"cols": 3})}
    # inlines = [LaboratoriumTaskParameterInline]
    extra = 0
    autocomplete_fields = ["product"]
