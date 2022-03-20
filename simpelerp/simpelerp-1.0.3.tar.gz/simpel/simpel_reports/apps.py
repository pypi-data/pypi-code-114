from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):
    icon = "chart-box-outline"
    name = 'simpel.simpel_reports'
    label = 'simpel_reports'
    verbose_name = 'Reports'
