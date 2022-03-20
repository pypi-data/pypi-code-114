import nested_admin
from django.contrib import admin

from simpel.simpel_products.admin import BundleAdmin

from .models import (  # InspectionCertificate,
    InspectionService,
    InspectionTask,
    InspectionTaskParameter,
)
from .resources import InspectionServiceResource

# from simpel.simpel_projects.admin import DeliverableChildAdmin, WorkOrderChildAdmin


@admin.register(InspectionService)
class InspectionServiceAdmin(BundleAdmin):
    inlines = BundleAdmin.inlines
    resource_class = InspectionServiceResource


class InspectionTaskParameterInline(nested_admin.SortableHiddenMixin, nested_admin.NestedTabularInline):
    model = InspectionTaskParameter
    extra = 0
    autocomplete_fields = ["parameter", "analysis_method"]


class InspectionTaskInline(nested_admin.SortableHiddenMixin, nested_admin.NestedStackedInline):
    model = InspectionTask
    # inlines = [InspectionTaskParameterInline]
    extra = 0
    autocomplete_fields = ["product"]
