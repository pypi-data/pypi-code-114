from django.apps import AppConfig


class SimpelProjectsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "simpel.simpel_projects"
    icon = "bulletin-board"
    label = "simpel_projects"
    verbose_name = "Projects"

    def ready(self):
        from . import signals  # NOQA
        return super().ready()
