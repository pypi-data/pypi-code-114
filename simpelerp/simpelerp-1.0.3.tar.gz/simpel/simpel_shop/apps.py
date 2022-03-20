from django.apps import AppConfig


class SimpelCartConfig(AppConfig):
    icon = "shopping-outline"
    default_auto_field = "django.db.models.BigAutoField"
    name = "simpel.simpel_shop"
    verbose_name = "Shopping"

    def ready(self):
        from django.contrib import admin

        from .models import CartItem
        from .settings import simpel_shop_settings as shop_settings

        if shop_settings.ADMIN:
            admin.site.register(CartItem, shop_settings.SHOP_ADMIN)
