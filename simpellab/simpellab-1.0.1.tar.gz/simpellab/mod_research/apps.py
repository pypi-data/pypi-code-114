from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SimpelSalesModlibConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    icon = "magnify-expand"
    name = "simpellab.mod_research"
    label = "mod_research"
    verbose_name = _("Simpel Research")


def init_permissions():
    pass
