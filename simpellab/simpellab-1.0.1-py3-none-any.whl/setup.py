from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.utils.text import slugify

from simpel.simpel_auth.utils import create_demo_users
from simpel.simpel_products.models import Bundle, BundleItem, Category, RecommendedItem, Service, Specification, Unit

group_names = [
    "Staff Customer Service",
    "Staff PJT",
    "Staff Sertifikat",
    "Staff invoicing",
    "Staff Bendahara Penerima",
]
user_names = {slugify(group).replace("-", "_"): group for group in group_names}


def reset_all():
    # Remove group and demo_users
    groups = Group.objects.filter(name__in=group_names)
    groups.delete()
    users = get_user_model().objects.filter(username__in=user_names)
    users.delete()
    init_permissions()
    init_demo_users()


def init_demo_users():
    create_demo_users(user_names)


def init_permissions():
    from django.contrib.auth.models import Group
    from django.db import transaction

    from simpel.simpel_auth.utils import add_group_perms, get_perms_dict
    from simpel.simpel_invoices.models import Invoice, InvoiceItem, InvoiceItemBundle
    from simpel.simpel_partners.models import Partner
    from simpel.simpel_payments.models import CashGateway, ManualTransferGateway, Payment, PaymentGateway
    from simpel.simpel_products.models import Inventory, Product
    from simpel.simpel_projects.models import CancelationDeliverable, Deliverable, DocumentDeliverable, Task, WorkOrder
    from simpel.simpel_sales.models import (
        ProformaInvoice, SalesOrder, SalesOrderItem, SalesOrderItemBundle, SalesQuotation, SalesQuotationItem,
        SalesQuotationItemBundle,
    )

    with transaction.atomic():
        customer_service, _ = Group.objects.get_or_create(name="Staff Customer Service")
        staff_pjt, _ = Group.objects.get_or_create(name="Staff PJT")
        staff_bendahara_penerima, _ = Group.objects.get_or_create(name="Staff Bendahara Penerima")
        staff_invoicing, _ = Group.objects.get_or_create(name="Staff invoicing")
        staff_sertifikat, _ = Group.objects.get_or_create(name="Staff Sertifikat")

        def_acts = ["view", "add", "change", "delete"]
        imex = ["import", "export"]

        # Simpel Partner
        partner = get_perms_dict(def_acts + imex + ["change_partner_user", "activate", "verify"], Partner)

        # Simpel Products
        unit = get_perms_dict(def_acts + imex, Unit)  # NOQA
        category = get_perms_dict(def_acts + imex, Category)  # NOQA
        specification = get_perms_dict(def_acts + imex, Specification)  # NOQA
        product = get_perms_dict(def_acts + imex, Product)
        inventory = get_perms_dict(def_acts + imex, Inventory)  # NOQA
        service = get_perms_dict(def_acts + imex, Service)  # NOQA
        bundle = get_perms_dict(def_acts + imex, Bundle)  # NOQA
        bundle_item = get_perms_dict(def_acts + imex, BundleItem)  # NOQA
        recom_item = get_perms_dict(def_acts + imex, RecommendedItem)  # NOQA

        # Simpel Sales
        salesorder = get_perms_dict(def_acts + imex + ["validate", "complete", "close"], SalesOrder)
        salesorder_item = get_perms_dict(def_acts + imex, SalesOrderItem)
        salesorder_item_bundle = get_perms_dict(def_acts + imex, SalesOrderItemBundle)
        salesquotation = get_perms_dict(def_acts + imex + ["validate", "close"], SalesQuotation)
        salesquotation_item = get_perms_dict(def_acts + imex, SalesQuotationItem)
        salesquotation_item_bundle = get_perms_dict(def_acts + imex, SalesQuotationItemBundle)
        proformainvoice = get_perms_dict(def_acts + imex, ProformaInvoice)

        # Simpel Projects
        workorder = get_perms_dict(def_acts + imex + ["validate", "process", "complete"], WorkOrder)
        task = get_perms_dict(def_acts + imex + ["complete"], Task)
        deliverable = get_perms_dict(def_acts + imex, Deliverable)
        cancelation_deliverable = get_perms_dict(def_acts + imex, CancelationDeliverable)
        document_deliverable = get_perms_dict(def_acts + imex, DocumentDeliverable)

        # Simpel Invoices
        invoice = get_perms_dict(def_acts + imex + ["validate", "cancel", "close"], Invoice)
        invoice_item = get_perms_dict(def_acts + imex, InvoiceItem)
        invoice_item_bundle = get_perms_dict(def_acts + imex, InvoiceItemBundle)

        # Simpel Payments
        payment = get_perms_dict(def_acts + imex + ["cancel", "validate", "reject", "approve"], Payment)
        payment_gateway = get_perms_dict(def_acts + imex, PaymentGateway)
        cash_gateway = get_perms_dict(def_acts + imex, CashGateway)
        manual_transfer_gateway = get_perms_dict(def_acts + imex, ManualTransferGateway)

        # CUSTOMER SERVICE
        # ======================================================================================
        # partner
        add_group_perms(customer_service, partner, ["view", "add", "change", "activate"])
        # product
        add_group_perms(customer_service, product, ["view"])
        # sales
        add_group_perms(customer_service, salesorder, ["view", "add", "change", "validate"])
        add_group_perms(customer_service, salesorder_item, ["view", "add", "change", "delete"])
        add_group_perms(customer_service, salesorder_item_bundle, ["view", "add", "change", "delete"])
        add_group_perms(customer_service, proformainvoice, ["view"])
        add_group_perms(customer_service, salesquotation, ["view", "add", "change", "validate"])
        add_group_perms(customer_service, salesquotation_item, ["view", "add", "change", "delete"])
        add_group_perms(customer_service, salesquotation_item_bundle, ["view", "add", "change", "delete"])
        # projects
        add_group_perms(customer_service, workorder, ["view", "add", "change"])
        add_group_perms(customer_service, task, ["view", "add", "change", "delete"])
        add_group_perms(customer_service, deliverable, ["view"])

        # STAFF PJT
        # ======================================================================================
        # partner
        add_group_perms(staff_pjt, partner, ["view", "add", "change", "activate", "verify"])

        # product
        add_group_perms(staff_pjt, product, ["view"])
        # sales
        add_group_perms(staff_pjt, salesorder, ["view", "add", "change", "validate", "close"])
        add_group_perms(staff_pjt, salesorder_item, ["view", "add", "change", "delete"])
        add_group_perms(staff_pjt, salesorder_item_bundle, ["view", "add", "change", "delete"])
        add_group_perms(staff_pjt, salesquotation, ["view", "add", "change"])
        add_group_perms(staff_pjt, salesquotation_item, ["view", "add", "change", "delete"])
        add_group_perms(staff_pjt, salesquotation_item_bundle, ["view", "add", "change", "delete"])
        add_group_perms(staff_pjt, proformainvoice, ["view", "add", "change"])
        # projects
        add_group_perms(staff_pjt, workorder, ["view", "add", "change", "validate", "process", "complete"])
        add_group_perms(staff_pjt, task, ["view", "add", "change", "delete"])
        add_group_perms(staff_pjt, deliverable, ["view"])
        # projects
        add_group_perms(staff_pjt, invoice, ["view"])

        # STAFF SERTIFIKAT
        # ======================================================================================
        add_group_perms(staff_sertifikat, partner, ["view"])

        add_group_perms(staff_sertifikat, salesorder, ["view", "add", "change"])
        add_group_perms(staff_sertifikat, workorder, ["view", "complete"])
        add_group_perms(staff_sertifikat, task, ["view", "change"])
        add_group_perms(staff_sertifikat, deliverable, ["view", "add", "change", "delete"])
        add_group_perms(staff_sertifikat, cancelation_deliverable, ["view", "add", "change", "delete"])
        add_group_perms(staff_sertifikat, document_deliverable, ["view", "add", "change", "delete"])

        # STAFF INVOICING
        # ======================================================================================
        # partner
        add_group_perms(staff_invoicing, partner, ["view"])

        # sales
        add_group_perms(staff_invoicing, salesorder, ["view", "validate", "close"])
        add_group_perms(staff_invoicing, salesquotation, ["view"])
        add_group_perms(staff_invoicing, proformainvoice, ["view"])

        # invoicing
        add_group_perms(staff_invoicing, invoice, ["view", "add", "change", "validate", "cancel", "close"])
        add_group_perms(staff_invoicing, invoice_item, ["view", "add", "change", "delete"])
        add_group_perms(staff_invoicing, invoice_item_bundle, ["view", "add", "change", "delete"])

        # STAFF BENDAHARA PENERIMA
        # ======================================================================================
        # partner
        add_group_perms(staff_bendahara_penerima, partner, ["view"])
        # product
        add_group_perms(staff_bendahara_penerima, product, ["view"])
        # sales
        add_group_perms(staff_bendahara_penerima, salesorder, ["view"])
        add_group_perms(staff_bendahara_penerima, salesquotation, ["view"])
        add_group_perms(staff_bendahara_penerima, proformainvoice, ["view"])
        # projects
        add_group_perms(staff_bendahara_penerima, workorder, ["view"])
        add_group_perms(staff_bendahara_penerima, task, ["view"])
        add_group_perms(staff_bendahara_penerima, deliverable, ["view"])
        # Invoices
        add_group_perms(staff_bendahara_penerima, invoice, ["view", "close"])
        # Payments
        add_group_perms(
            staff_bendahara_penerima,
            payment,
            [
                "view",
                "add",
                "change",
                "validate",
                "approve",
                "reject",
                "cancel",
            ],
        )
        add_group_perms(staff_bendahara_penerima, payment_gateway, ["view"])
        add_group_perms(staff_bendahara_penerima, cash_gateway, ["view"])
        add_group_perms(staff_bendahara_penerima, manual_transfer_gateway, ["view"])
