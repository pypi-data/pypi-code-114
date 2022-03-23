from django.apps import AppConfig
from django.conf import settings
from django.db.models.signals import post_migrate
from django.utils.translation import gettext_lazy as _


class SimpelProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "simpel_products"
    label = "simpel_products"
    verbose_name = _("Products")

    def ready(self):
        post_migrate.connect(init_app, sender=self)


def init_app(**kwargs):
    pass


def init_demo_users():
    # from simpel.simpel_auth.utils import create_demo_users

    # usernames = {
    #     "products_manager": "Products Manager",
    #     "products_admin": "Products Admin",
    # }
    # create_demo_users(usernames)
    pass


def init_permissions():
    # from django.contrib.auth.models import Group
    # from django.db import transaction

    # from simpel.simpel_auth.utils import add_perms, get_perms_dict
    # from simpel.simpel_products import models

    # with transaction.atomic():
    #     products_manager, _ = Group.objects.get_or_create(name="Products Manager")
    #     products_admin, _ = Group.objects.get_or_create(name="Products Admin")

    #     def_acts = ["view", "add", "change", "delete"]
    #     imex_acts = ["import", "export"]

    #     unit = get_perms_dict(def_acts + imex_acts, models.Unit)
    #     category = get_perms_dict(def_acts + imex_acts, models.Category)
    #     specification = get_perms_dict(def_acts + imex_acts, models.Specification)
    #     product = get_perms_dict(def_acts + imex_acts, models.Product)
    #     inventory = get_perms_dict(def_acts + imex_acts, models.Inventory)
    #     service = get_perms_dict(def_acts + imex_acts, models.Service)
    #     bundle = get_perms_dict(def_acts + imex_acts, models.Bundle)
    #     bundle_item = get_perms_dict(def_acts + imex_acts, models.BundleItem)
    #     recom_item = get_perms_dict(def_acts + imex_acts, models.RecommendedItem)

    #     products_manager_perms = [
    #         # View
    #         product["view"],
    #         unit["view"],
    #         category["view"],
    #         bundle["view"],
    #         bundle_item["view"],
    #         recom_item["view"],
    #         inventory["view"],
    #         service["view"],
    #         specification["view"],
    #         # Add
    #         unit["add"],
    #         category["add"],
    #         bundle_item["add"],
    #         recom_item["add"],
    #         product["add"],
    #         inventory["add"],
    #         service["add"],
    #         specification["add"],
    #         # Change
    #         unit["change"],
    #         category["change"],
    #         bundle["change"],
    #         bundle_item["change"],
    #         recom_item["change"],
    #         product["change"],
    #         inventory["change"],
    #         service["change"],
    #         specification["change"],
    #         # Import Export
    #     ]
    #     products_admin_perms = products_manager_perms + [
    #         unit["delete"],
    #         category["delete"],
    #         bundle["delete"],
    #         bundle_item["delete"],
    #         recom_item["delete"],
    #         product["delete"],
    #         inventory["delete"],
    #         service["delete"],
    #         specification["delete"],
    #         # IMPORT
    #         unit["import"],
    #         category["import"],
    #         bundle["import"],
    #         bundle_item["import"],
    #         recom_item["import"],
    #         product["import"],
    #         inventory["import"],
    #         service["import"],
    #         specification["import"],
    #         # EXPORT
    #         unit["export"],
    #         category["export"],
    #         bundle["export"],
    #         bundle_item["export"],
    #         recom_item["export"],
    #         product["export"],
    #         inventory["export"],
    #         service["export"],
    #         specification["export"],
    #     ]
    #     add_perms(products_manager, products_manager_perms)
    #     add_perms(products_admin, products_admin_perms)
    pass

