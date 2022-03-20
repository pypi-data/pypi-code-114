import logging

from django.db import transaction

# from .models import Entry, Transaction
from .settings import simpel_accounts_settings as accounts_setting

# from django.dispatch import receiver

# from simpel.simpel_core.signals import (
#     post_cancel,
#     post_confirm,
#     post_process,
#     post_validate,
# )


# from simpel.simpel_invoices.models import Invoice
# from simpel.simpel_payments.models import Receipt
# from simpel.simpel_sales.models import SalesOrder


# from .utils import get_cash_account, get_partner_payable_account

logger = logging.getLogger("engine")
names = accounts_setting.NAMES


# @receiver(post_save, sender=ManualTransferGateway)
# def after_save_payment_gateway(sender, instance, created, raw, using, **kwargs):
#     account, _ = get_cash_account(instance)


# @receiver(post_save, sender=CashGateway)
# def after_save_cash_gateway(sender, instance, created, raw, using, **kwargs):
#     account, _ = get_cash_account(instance)


# Transactions Events
# ========================================


# @receiver(post_process, sender=SalesOrder)
def after_validate_salesorder(sender, instance, actor, request, **kwargs):
    # post_process SalesOrder
    # Trx 1
    # # PYMHD                 D
    # # -- PYMHD Reverse      C
    print("After process Sales Order signal simpel_sales")


# @receiver(post_confirm, sender=Receipt)
def after_confirm_receipt(sender, instance, actor, request, **kwargs):
    # post_confirm Receipt -> SalesOrder (Confirm BKM Pembayaran Uang Muka)
    # # Trx 1 ref SalesOrder
    # # Cash Account          D
    # # -- Account PDM        C
    # # Trx 2
    # # PYMHD Reverse         D
    # # -- PYMHD              C
    with transaction.atomic():

        if instance.reference_type.model == "salesorder":
            print("Transaction -> Sales Order signal simpel_accounts")
            # partner_payable = get_partner_payable_account(instance.source)
            # cash_account = get_cash_account(instance.destination)
            # trx = Transaction(reference=instance, note="Downpayment Sales Order #%s" % instance.inner_id)
            # trx.save()
            # entry1 = Entry(trx=trx, account=cash_account, flow=Entry.DEBIT, amount=instance.amount)
            # entry2 = Entry(trx=trx, account=partner_payable, flow=Entry.CREDIT, amount=instance.amount)
            # entry1.save()
            # entry2.save()
            # # recompute all
            # trx.status = Transaction.CONFIRMED
            # trx.save()

        # post_confirm Receipt -> Invoice (Confirm BKM Pelunasan)
        # # Trx 1 ref Receipt
        # # Cash Account          D
        # # -- Account Receivable C
        if instance.reference_type.model == "invoice":
            print("Transaction: Confirm Receipt -> Invoice signal simpel_accounts")


# @receiver(post_validate, sender=Invoice)
def after_validate_invoice(sender, instance, actor, request, **kwargs):
    # post_validate Invoice
    # # Trx 1 ref Invoice
    # # Account Receivable    D
    # # Account PDM           D
    # # -- Revenue            C
    # # Trx 2
    # # PYMHD Reverse         D
    # # -- PYMHD              C
    print("Transaction 1 : Record Piutang")
    print("Transaction 2 : Record PYMHD")


# Transactions Reverse Event
# ========================================


# @receiver(post_cancel, sender=SalesOrder)
def after_cancel_valid_salesorder(sender, instance, actor, request, **kwargs):
    # post_cancel SalesOrder
    # Trx 1 -> Ref SalesOrder -> Memo Cancelation
    # # PYMHD Reverse         D
    # # -- PYMHD              C
    print("Reverse Transaction: cancel Sales Order signal simpel_sales")


# @receiver(post_cancel, sender=Receipt)
def after_cancel_confirmed_receipt(sender, instance, actor, request, **kwargs):
    # post_cancel Receipt -> SalesOrder (Cancel BKM Pembayaran Uang Muka)
    # # Trx 1 ref SalesOrder
    # # Account PDM           D
    # # -- Cash Account       C
    # # Trx 2
    # # PYMHD                 D
    # # -- PYMHD Reverse      C
    if instance.reference_type.model == "salesorder":
        print("Cancel Receipt -> Sales Order signal simpel_accounts")

    # post_cancel Receipt -> Invoice (Confirm BKM Pelunasan)
    # # Trx 1 ref Receipt
    # # Account Receivable    D
    # # -- Cash Account       C
    if instance.reference_type.model == "invoice":
        print("Cancel Receipt -> Invoice signal simpel_accounts")


# @receiver(post_cancel, sender=Invoice)
def after_cancel_valid_invoice(sender, instance, actor, request, **kwargs):
    # post_cancel Invoice
    # # Trx 1 ref Invoice
    # # Revenue               D
    # # -- Account PDM        C
    # # -- Account Receivable C
    # # Trx 2
    # # PYMHD                 D
    # # -- PYMHD Reverse      C
    print("Transaction 1 : Record Piutang")
    print("Transaction 2 : Record PYMHD")
