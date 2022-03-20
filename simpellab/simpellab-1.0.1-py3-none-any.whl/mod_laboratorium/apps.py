from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SimpelabModLaboratoriumConfig(AppConfig):
    icon = "flask"
    name = "simpellab.mod_laboratorium"
    label = "mod_laboratorium"
    default_auto_field = "django.db.models.BigAutoField"
    verbose_name = _("Simpel Laboratorium")


def init_permissions():
    pass
