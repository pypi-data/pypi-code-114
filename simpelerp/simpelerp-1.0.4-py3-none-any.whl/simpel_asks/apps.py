from django.apps import AppConfig


class SimpelAsksConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "simpel.simpel_asks"
    app_label = "simpel_asks"
    verbose_name = "Questions"
    icon = "tooltip-text-outline"
