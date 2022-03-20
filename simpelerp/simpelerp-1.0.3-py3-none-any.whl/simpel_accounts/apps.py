from django.apps import AppConfig


class SimpelAccountsConfig(AppConfig):
    icon = "cash-100"
    default_auto_field = "django.db.models.BigAutoField"
    name = "simpel.simpel_accounts"
    app_label = "simpel_accounts"
    verbose_name = "Accounts"

    def ready(self):
        from . import signals  # NOQA
        return super().ready()
