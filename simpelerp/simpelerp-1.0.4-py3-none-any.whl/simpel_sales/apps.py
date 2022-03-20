from django.apps import AppConfig
from django.db.models.signals import post_migrate


class SimpelSalesConfig(AppConfig):
    icon = "handshake-outline"
    default_auto_field = "django.db.models.BigAutoField"
    name = "simpel.simpel_sales"
    label = "simpel_sales"
    verbose_name = "Sales"

    def ready(self):
        from simpel.simpel_sales import signals  # NOQA

        post_migrate.connect(init_app, sender=self)
        return super().ready()


def init_app(**kwargs):
    pass


def init_demo_users():
    from simpel.simpel_auth.utils import create_demo_users

    usernames = {
        "sales_staff": "Sales Staff",
        "sales_supervisor": "Sales Supervisor",
        "sales_manager": "Sales Manager",
        "sales_admin": "Sales Admin",
    }
    create_demo_users(usernames)


def init_permissions():
    from django.contrib.auth.models import Group
    from django.db import transaction

    from simpel.simpel_auth.utils import add_perms, get_perms_dict
    from simpel.simpel_sales import models

    sales_staff, _ = Group.objects.get_or_create(name="Sales Staff")
    sales_supervisor, _ = Group.objects.get_or_create(name="Sales Supervisor")
    sales_manager, _ = Group.objects.get_or_create(name="Sales Manager")
    sales_admin, _ = Group.objects.get_or_create(name="Sales Admin")

    # default actions
    def_acts = ["view", "add", "change", "delete"]
    imex = ["export", "import"]

    salesorder = get_perms_dict(def_acts + imex + ["validate", "close"], models.SalesOrder)
    salesorder_item = get_perms_dict(def_acts + imex, models.SalesOrderItem)
    salesorder_item_bundle = get_perms_dict(def_acts + imex, models.SalesOrderItemBundle)
    quotation = get_perms_dict(def_acts + imex + ["validate", "close"], models.SalesQuotation)
    quotation_item = get_perms_dict(def_acts + imex, models.SalesQuotationItem)
    quotation_item_bundle = get_perms_dict(def_acts + imex, models.SalesQuotationItemBundle)
    proforma = get_perms_dict(def_acts + imex, models.ProformaInvoice)

    sales_staff_perms = [
        # View
        salesorder["view"],
        salesorder_item["view"],
        salesorder_item_bundle["view"],
        quotation["view"],
        quotation_item["view"],
        quotation_item_bundle["view"],
        proforma["view"],
        # Add
        salesorder["add"],
        salesorder_item["add"],
        salesorder_item_bundle["add"],
        quotation["add"],
        quotation_item["add"],
        quotation_item_bundle["add"],
        # Change
        salesorder["change"],
        salesorder_item["change"],
        salesorder_item_bundle["change"],
        quotation["change"],
        quotation_item["change"],
        quotation_item_bundle["change"],
        # Delete
        salesorder_item["delete"],
        salesorder_item_bundle["delete"],
        quotation_item["delete"],
        quotation_item_bundle["delete"],
        # Validation
        salesorder["validate"],
        quotation["validate"],
    ]
    sales_supervisor_perms = sales_staff_perms + [salesorder["close"]]
    sales_manager_perms = sales_supervisor_perms
    sales_admin_perms = sales_manager_perms + [
        salesorder["delete"],
        quotation["delete"],
    ]

    with transaction.atomic():
        add_perms(sales_staff, sales_staff_perms)
        add_perms(sales_supervisor, sales_supervisor_perms)
        add_perms(sales_manager, sales_manager_perms)
        add_perms(sales_admin, sales_admin_perms)
