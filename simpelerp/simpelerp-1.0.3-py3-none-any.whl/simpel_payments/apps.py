from django.apps import AppConfig


class SimpelPaymentsConfig(AppConfig):
    icon = "credit-card-check-outline"
    default_auto_field = "django.db.models.BigAutoField"
    name = "simpel.simpel_payments"
    label = "simpel_payments"
    verbose_name = "Payments"

    def ready(self):
        from simpel.simpel_payments import signals  # NOQA

        return super().ready()
