from django.apps import AppConfig


class FormGeneratorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'form_schema_generator'

    def ready(self):
        from . import generator
        generator.FORM_GENERATABLE_URLS = generator.get_url_choices()

