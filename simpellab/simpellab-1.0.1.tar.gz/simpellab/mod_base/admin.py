from django.contrib import admin
from django.utils.safestring import mark_safe
from import_export.admin import ImportExportMixin
from simpel.simpel_products.admin import ProductChildAdmin

from .models import AnalysisMethod, Parameter
from .resources import AnalysisMethodResource, ParameterResource


@admin.register(AnalysisMethod)
class AnalysisMethodAdmin(ImportExportMixin, admin.ModelAdmin):
    search_fields = ["name", "slug", "reference"]
    list_display = ["name", "slug", "reference"]
    resource_class = AnalysisMethodResource


@admin.register(Parameter)
class ParameterAdmin(ProductChildAdmin):
    list_filters = ["category"]
    list_display = ["inner_id", "name", "unit", "code", "price"]
    search_fields = ["name"]
    inlines = []
    raw_id_fields = ["parent", "analysis_method"]
    resource_class = ParameterResource
    fields = ProductChildAdmin.fields + [
        "analysis_method",
        "unit_code",
        "price",
    ]

    def get_resource_class(self):
        return super().get_resource_class()

    def code(self, obj):
        return mark_safe(obj.unit_code) if obj.unit_code else "-"
