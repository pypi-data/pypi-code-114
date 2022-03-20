from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SimpelModSalesConfig(AppConfig):
    icon = "sale-outline"
    name = "simpellab.mod_sales"
    label = "mod_sales"
    verbose_name = _("Simpel Sales")
    default_auto_field = "django.db.models.BigAutoField"
