from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SimpelInvoicesConfig(AppConfig):
    icon = "inbox-full-outline"
    default_auto_field = "django.db.models.BigAutoField"
    name = "simpel.simpel_invoices"
    label = "simpel_invoices"
    verbose_name = _("Invoices")

    def ready(self):
        from . import signals  # NOQA

        return super().ready()
