from django.contrib import admin

from polymorphic.admin import PolymorphicChildModelAdmin, PolymorphicParentModelAdmin

from .models import Category, FileModelTemplate, ModelTemplate, PathModelTemplate, StringModelTemplate
from .settings import simpel_core_settings as core_settings
from .views import EditCurrentSiteSetting, EditSetting


def admin_settings_edit(request, app_name, model_name, site_pk):
    context = {**admin.site.each_context(request)}
    return EditSetting.as_view(extra_context=context)(request, app_name, model_name, site_pk)


def settings_edit_current_site(request, app_name, model_name):
    context = {**admin.site.each_context(request)}
    return EditCurrentSiteSetting.as_view(extra_context=context)(request, app_name, model_name)


def settings_view(request, extra_context=None):
    return settings_edit_current_site(request, "simpel_core", "generalsetting")


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


admin.site.register(ModelTemplate, core_settings.MODEL_TEMPLATE_ADMIN)
admin.site.register(FileModelTemplate, core_settings.FILE_MODEL_TEMPLATE_ADMIN)
admin.site.register(PathModelTemplate, core_settings.PATH_MODEL_TEMPLATE_ADMIN)
admin.site.register(StringModelTemplate, core_settings.STRING_MODEL_TEMPLATE_ADMIN)
