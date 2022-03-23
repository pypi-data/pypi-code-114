from django.apps import AppConfig
from django.conf import settings
from django.db.models.signals import post_migrate
from django.utils.translation import gettext_lazy as _


class SimpelJournalsConfig(AppConfig):
    icon = "cash-100"
    default_auto_field = "django.db.models.BigAutoField"
    name = "simpel_journals"
    app_label = "simpel_journals"
    verbose_name = "Journals"

    def ready(self):
        from . import signals  # NOQA
        post_migrate.connect(init_app, sender=self)

def init_app(sender, **kwargs):
    pass
