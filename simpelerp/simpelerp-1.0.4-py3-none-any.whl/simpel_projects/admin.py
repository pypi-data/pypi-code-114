from django.contrib import admin, messages
from django.utils.translation import gettext_lazy as _

from import_export.admin import ImportExportMixin
from polymorphic.admin import (
    PolymorphicChildModelAdmin, PolymorphicInlineSupportMixin, PolymorphicParentModelAdmin, StackedPolymorphicInline,
)

from simpel.simpel_admin.base import AdminPrintViewMixin, ModelAdminMixin
from simpel.simpel_auth.admin import AdminActivityMixin, SingleLinkedAddressInline

from .helpers import get_deliverable_childs_models, get_task_childs_models, get_workorder_childs_models
from .models import CancelationDeliverable, Deliverable, DocumentDeliverable, FinalDocument, Task, WorkOrder
from .settings import simpel_projects_settings as projects_settings


class TaskPolymorphicInline(StackedPolymorphicInline):
    model = Task

    def get_child_models(self):
        """
        Register child model using defaults from settings
        """
        # Get deliverable child models map from hooks
        child_models = get_task_childs_models()
        child_models += [Task]
        return child_models

    def get_child_inline_classes(self):
        child_models = self.get_child_models()
        child_inlines = []
        for child in child_models:
            class_name = child.__class__.__name__
            props = {"model": child}
            parent_class = (StackedPolymorphicInline.Child,)
            inline_class = type("%sInline" % class_name, parent_class, props)
            child_inlines.append(inline_class)
        return child_inlines

    def get_child_inline_instances(self):
        instances = []
        for ChildInlineType in self.get_child_inline_classes():
            instances.append(ChildInlineType(parent_inline=self))
        return instances


class WorkOrderAdminBase(
    PolymorphicInlineSupportMixin,
    ImportExportMixin,
    AdminPrintViewMixin,
    AdminActivityMixin,
    ModelAdminMixin,
):
    inlines = [TaskPolymorphicInline]
    # autocomplete_fields = ["customer"]
    readonly_fields = ["status", "group"]
    search_fields = ["inner_id", "title", "reference_id"]
    actions = [
        "validate_action",
        "complete_action",
    ]
    list_filter = ["status"]
    date_hierarchy = "created_at"
    list_display = [
        "inner_id",
        "reference_id",
        "progress",
        "status",
        "object_buttons",
    ]

    def has_change_permission(self, request, obj=None):
        default = super().has_change_permission(request, obj)
        if obj:
            return obj.is_editable and default
        else:
            return default

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["customer", "reference_type", "reference_id"]
        return super().get_readonly_fields(request, obj)


class PolymorphicWorkOrderAdmin(WorkOrderAdminBase, PolymorphicParentModelAdmin):
    child_models = [WorkOrder]
    parent_include = True

    def get_child_models(self):
        """
        Register child model using defaults from settings

        """
        super_child_models = super().get_child_models()
        child_models = list(super_child_models).copy()
        # Get deliverable child models map from hooks
        child_models = get_workorder_childs_models()

        if len(child_models) == 0:
            child_models = [WorkOrder]
        if self.parent_include and WorkOrder not in child_models:
            child_models += [WorkOrder]
        return child_models


class DeliverablePolymorphicInline(StackedPolymorphicInline):
    model = Deliverable

    def has_change_permission(self, request, obj=None):
        if obj and obj.workorder.status == WorkOrder.VALID and not obj.progress_complete:
            return super().has_change_permission(request, obj)
        else:
            False

    def get_child_models(self):
        """
        Register child model using defaults from settings
        """
        # Get deliverable child models map from hooks
        child_models = get_deliverable_childs_models()
        if len(child_models) == 0:
            child_models = [Deliverable, CancelationDeliverable]
        return child_models

    def get_child_inline_classes(self):
        child_models = self.get_child_models()
        child_inlines = []
        for child in child_models:
            class_name = child.__class__.__name__
            props = {"model": child, "fields": child.formset_fields}
            parent_class = (StackedPolymorphicInline.Child,)
            inline_class = type("%sInline" % class_name, parent_class, props)
            child_inlines.append(inline_class)
        return child_inlines

    def get_child_inline_instances(self):
        instances = []
        for ChildInlineType in self.get_child_inline_classes():
            instances.append(ChildInlineType(parent_inline=self))
        return instances


class TaskAdmin(PolymorphicInlineSupportMixin, ModelAdminMixin):
    search_fields = [
        "inner_id",
        "reference_id",
        "workorder__inner_id",
        "workorder__reference_id",
    ]
    list_display = [
        "inner_id",
        "name",
        "reference",
        "quantity",
        "completes",
        "progress",
    ]
    fields = [
        "position",
        "workorder",
        "reference_id",
        "start_at",
        "end_at",
        "quantity",
    ]
    readonly_fields = fields
    inlines = [SingleLinkedAddressInline, DeliverablePolymorphicInline]

    # def has_change_permission(self, request, obj=None):
    #     if obj and obj.workorder.status == WorkOrder.VALID and not obj.progress_complete:
    #         return super().has_change_permission(request, obj)
    #     else:
    #         False


class DeliverableAdminBase(ModelAdminMixin):
    search_fields = ["inner_id", "customer__name", "order_item__inner_id"]
    list_display = ["inner_id", "name", "customer"]
    autocomplete_fields = ["task"]
    inspect_template = "admin/simpel_projects/deliverable_inspect.html"


class DeliverableAdmin(DeliverableAdminBase, PolymorphicParentModelAdmin):
    child_models = [CancelationDeliverable, DocumentDeliverable]
    list_display = ["inner_id", "task", "customer", "created_at"]

    def get_child_models(self):
        """
        Register child model using defaults from settings

        """
        super_child_models = super().get_child_models()
        child_models = list(super_child_models).copy()
        # Get deliverable child models map from hooks
        child_models = get_deliverable_childs_models()
        if len(child_models) == 0:
            child_models = [Deliverable, CancelationDeliverable]
        return child_models


class DeliverableChildAdmin(DeliverableAdminBase, PolymorphicChildModelAdmin):
    show_in_index = True


class CancelationDeliverableAdmin(DeliverableChildAdmin):
    list_display = ["inner_id", "customer", "created_at"]


class DocumentDeliverableAdmin(DeliverableChildAdmin):
    list_display = ["inner_id", "customer", "created_at"]


class FinalDocumentAdmin(AdminPrintViewMixin, AdminActivityMixin, ModelAdminMixin):
    print_template = "admin/finaldocument_print.html"
    list_filter = ["status"]
    search_fields = ["inner_id", "workorder__inner_id", "workorder__cunstomer__name"]
    readonly_fields = ["workorder", "user"]
    actions = ["mark_as_complete"]

    def has_add_permission(self, request):
        return False

    def mark_as_complete(self, request, queryset):
        try:
            for obj in queryset:
                obj.complete(request)
            if obj.status == obj.PROCESSED:
                messages.success(request, _("%s complete.") % obj)
        except PermissionError as err:
            messages.error(request, err)


admin.site.register(WorkOrder, projects_settings.WORKORDER_ADMIN)
admin.site.register(Task, projects_settings.TASK_ADMIN)
admin.site.register(Deliverable, projects_settings.DELIVERABLE_ADMIN)
admin.site.register(CancelationDeliverable, projects_settings.CANCELATION_DELIVERABLE_ADMIN)
admin.site.register(DocumentDeliverable, projects_settings.DOCUMENT_DELIVERABLE_ADMIN)
admin.site.register(FinalDocument, projects_settings.FINAL_DOCUMENT_ADMIN)
