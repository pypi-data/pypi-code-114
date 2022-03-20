from django.apps import AppConfig


class SimpellabBaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'simpellab.mod_blueprints'
    label = 'mod_blueprints'
    verbose_name = 'Simpel Blueprints'
    icon = 'text-box-outline'
