from django.contrib import admin

from huscy.attributes import models
from huscy.attributes.services import _create_attribute_category_permissions


class AttributeSchemaAdmin(admin.ModelAdmin):
    list_display = 'id', 'schema'
    list_display_links = None

    def save_model(self, request, attribute_schema, form, change):
        super().save_model(request, attribute_schema, form, change)
        _create_attribute_category_permissions(attribute_schema.schema)

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class AttributeSetAdmin(admin.ModelAdmin):
    list_display = 'pseudonym', '_attribute_schema', 'attributes'

    def _attribute_schema(self, attribute_set):
        return attribute_set.attribute_schema.id

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(models.AttributeSchema, AttributeSchemaAdmin)
admin.site.register(models.AttributeSet, AttributeSetAdmin)
