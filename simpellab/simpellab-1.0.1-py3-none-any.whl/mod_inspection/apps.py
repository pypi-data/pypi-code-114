from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SimpelSalesModlitConfig(AppConfig):
    icon = "incognito"
    default_auto_field = "django.db.models.BigAutoField"
    name = "simpellab.mod_inspection"
    label = "mod_inspection"
    verbose_name = _("Simpel Inspection")


def init_permissions():
    pass
