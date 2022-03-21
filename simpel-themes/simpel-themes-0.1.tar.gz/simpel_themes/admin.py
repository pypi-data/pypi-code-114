from django.contrib import admin

from polymorphic.admin import PolymorphicChildModelAdmin, PolymorphicParentModelAdmin

from .models import Category, FileModelTemplate, ModelTemplate, PathModelTemplate, StringModelTemplate
from .settings import themes_settings


@admin.register(Category)
class TemplateCategory(admin.ModelAdmin):
    list_display = ["name"]


class ModelTemplateAdmin(PolymorphicParentModelAdmin):
    child_models = [
        FileModelTemplate,
        PathModelTemplate,
        StringModelTemplate,
    ]


class FileModelTemplateAdmin(PolymorphicChildModelAdmin):
    index = False


class PathModelTemplateAdmin(PolymorphicChildModelAdmin):
    index = False


class StringModelTemplateAdmin(PolymorphicChildModelAdmin):
    index = False


admin.site.register(ModelTemplate, themes_settings.MODEL_TEMPLATE_ADMIN)
admin.site.register(FileModelTemplate, themes_settings.FILE_MODEL_TEMPLATE_ADMIN)
admin.site.register(PathModelTemplate, themes_settings.PATH_MODEL_TEMPLATE_ADMIN)
admin.site.register(StringModelTemplate, themes_settings.STRING_MODEL_TEMPLATE_ADMIN)
