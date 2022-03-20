from django.apps import AppConfig


class SimpellabBaseConfig(AppConfig):
    icon = "database-clock-outline"
    default_auto_field = "django.db.models.BigAutoField"
    name = "simpellab.mod_base"
    label = "simpellab"
    verbose_name = "Simpellab"
