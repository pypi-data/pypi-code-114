from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SimpelSalesModkslConfig(AppConfig):
    icon = "account-supervisor-circle-outline"
    name = "simpellab.mod_consultancy"
    label = "mod_consultancy"
    verbose_name = _("Simpel Consultancy")
    default_auto_field = "django.db.models.BigAutoField"


def init_permissions():
    pass
