from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SimpelSalesModproConfig(AppConfig):
    icon = "certificate-outline"
    default_auto_field = "django.db.models.BigAutoField"
    name = "simpellab.mod_certification"
    label = "mod_certification"
    verbose_name = _("Simpel Product Certification")


def init_permissions():
    pass
