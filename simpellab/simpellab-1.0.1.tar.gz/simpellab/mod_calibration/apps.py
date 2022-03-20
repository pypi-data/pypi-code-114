from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SimpelModkalConfig(AppConfig):
    icon = "cog-sync-outline"
    default_auto_field = "django.db.models.BigAutoField"
    name = "simpellab.mod_calibration"
    label = "mod_calibration"
    verbose_name = _("Simpel Calibration")


def init_permissions():
    pass
