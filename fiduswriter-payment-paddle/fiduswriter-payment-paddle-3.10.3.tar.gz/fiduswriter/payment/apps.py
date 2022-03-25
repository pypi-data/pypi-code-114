from django.apps import AppConfig


class Config(AppConfig):
    name = "payment"
    default_auto_field = "django.db.models.AutoField"

    def ready(self):
        from payment import signals  # noqa
