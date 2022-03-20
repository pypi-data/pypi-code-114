from django_hookup import core as hookup

from .admin import admin_settings_edit, settings_edit_current_site, settings_view


@hookup.register("REGISTER_ADMIN_VIEW")
def register_setting_edit_current_view():
    return (
        "settings/<str:app_name>/<str:model_name>/",
        settings_edit_current_site,
        "settings_edit",
    )


@hookup.register("REGISTER_ADMIN_VIEW")
def register_setting_edit_view():
    return (
        "settings/<str:app_name>/<str:model_name>/<int:site_pk>/",
        admin_settings_edit,
        "settings_edit",
    )


@hookup.register("REGISTER_ADMIN_VIEW")
def register_settings_view():
    return ("settings/", settings_view, "settings")
