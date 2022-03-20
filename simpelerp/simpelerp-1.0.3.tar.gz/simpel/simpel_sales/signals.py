from django.db.models.signals import ModelSignal, post_delete, post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from simpel.simpel_auth.tasks import send_notification_job
from simpel.simpel_core.signals import post_validate
from simpel.simpel_sales.models import (
    SalesOrder,
    SalesOrderItem,
    SalesOrderItemBundle,
    SalesQuotation,
    SalesQuotationItem,
    SalesQuotationItemBundle,
)

after_checkout = ModelSignal(use_caching=True)

salesorder_checkout_notif_group = ["Customer Service", "Sales Admin"]
salesorder_validation_notif_group = ["Customer Service", "Accounting", "Sales Admin"]
salesorder_close_notif_group = ["Invoicing", "Sales Admin"]

# Sales Order Signals


@receiver(post_save, sender=SalesOrder)
def after_save_order(sender, instance, created, **kwargs):
    print(instance.admin_url)
    if instance.qrcodes.first() is None:
        instance.qrcodes.create(name="public_url", qrcode_data=instance.admin_url)


@receiver(after_checkout, sender=SalesOrder)
def after_checkout_order(sender, instance, actor, **kwargs):
    send_notification_job.delay(
        actor_id=actor.id,
        groups=salesorder_checkout_notif_group,
        verb=_("create"),
        object_model=sender,
        object_id=instance.id,
    )


@receiver(post_validate, sender=SalesOrder)
def after_validate_salesorder(sender, instance, actor, **kwargs):
    from simpel.simpel_sales.models import ProformaInvoice

    proforma, created = ProformaInvoice.objects.get_or_create(salesorder=instance)
    send_notification_job.delay(
        actor_id=actor.id,
        groups=salesorder_validation_notif_group,
        verb=_("validate"),
        object_model=sender,
        object_id=instance.id,
        target_model=ProformaInvoice,
        target_id=proforma.id,
    )


# def pre_process_action(self):
#     work_order = getattr(self, "work_order", None)
#     if work_order is None:
#         raise PermissionError(_("Can't be processed there is no work order linked to this sales order."))
#     if work_order.status != const.VALID:
#         raise PermissionError(
#             _("Can't be processed work order status that linked to this sales order is not valid.")
#         )

# def pre_complete_action(self):
#     reference = getattr(self, "final_document", None)
#     if reference is None:
#         raise PermissionError(_("Can't complete this order there no final document linked to this sales order."))
#     if reference.status != const.COMPLETE:
#         raise PermissionError(
#             _("Can't complete this order, final document status that linked to this sales order is not complete.")
#         )
#     pass

# def pre_invoicing_action(self, request=None):
#     pass

# def post_invoicing_action(self, request=None):
#     pass


@receiver(post_save, sender=SalesOrderItem)
def after_save_salesorder_item(sender, instance, created, raw, using, **kwargs):
    instance.salesorder.save()


@receiver(post_save, sender=SalesOrderItemBundle)
def after_save_salesorder_item_bundle(sender, instance, created, raw, using, **kwargs):
    instance.item.save()


@receiver(post_delete, sender=SalesOrderItem)
def after_delete_salesorder_item(sender, instance, **kwargs):
    instance.salesorder.save()


@receiver(post_delete, sender=SalesOrderItemBundle)
def after_delete_salesorder_item_bundle(sender, instance, **kwargs):
    instance.item.save()


# Sales Quotation Signals


@receiver(post_save, sender=SalesQuotation)
def after_save_quotation(sender, instance, created, **kwargs):
    if instance.qrcodes.first() is None:
        instance.qrcodes.create(name="public_url", qrcode_data=instance.admin_url)


@receiver(after_checkout, sender=SalesQuotation)
def after_checkout_quotation(sender, instance, actor, **kwargs):
    send_notification_job.delay(
        actor_id=actor.id,
        groups=["Customer Service"],
        verb="membuat",
        object_model=sender,
        object_id=instance.id,
    )


@receiver(post_save, sender=SalesQuotationItem)
def after_save_salesquotation_item(sender, instance, created, raw, using, **kwargs):
    instance.salesquotation.save()


@receiver(post_save, sender=SalesQuotationItemBundle)
def after_save_salesquotation_item_bundle(sender, instance, created, raw, using, **kwargs):
    instance.item.save()


@receiver(post_delete, sender=SalesQuotationItem)
def after_delete_salesquotation_item(sender, instance, **kwargs):
    instance.salesquotation.save()


@receiver(post_delete, sender=SalesQuotationItemBundle)
def after_delete_salesquotation_item_bundle(sender, instance, **kwargs):
    instance.item.save()


@receiver(post_validate, sender=SalesOrder)
def after_validate_salesorder_bundle(sender, instance, **kwargs):
    print("After validate Sales Order signal simpel_sales")
