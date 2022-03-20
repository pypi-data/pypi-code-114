from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SimpelModlatConfig(AppConfig):
    icon = "school-outline"
    name = "simpellab.mod_training"
    label = "mod_training"
    verbose_name = _("Simpel Training")
    default_auto_field = "django.db.models.BigAutoField"


def init_permissions():
    pass
