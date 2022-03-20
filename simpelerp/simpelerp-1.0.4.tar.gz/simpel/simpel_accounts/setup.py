from django.db import transaction
from django_hookup import core as hookup

from simpel.simpel_accounts.models import AccountType
from simpel.simpel_accounts.utils import get_cash_account
from simpel.simpel_payments.models import CashGateway, ManualTransferGateway

from .settings import simpel_accounts_settings

names = simpel_accounts_settings.NAMES


@transaction.atomic
def create_default_accounts():
    """Create the default structure"""
    get_or_create_type = AccountType.objects.get_or_create
    asset, _ = get_or_create_type(name=names["ASSET"])
    asset.save()
    cash, _ = get_or_create_type(parent=asset, name=names["CASH"])
    cash.save()
    petty_cash, _ = get_or_create_type(parent=cash, name=names["PETTY_CASH"])
    petty_cash.save()
    bank_cash, _ = get_or_create_type(parent=cash, name=names["BANK"])
    bank_cash.save()

    for cash_gateway in CashGateway.objects.all():
        get_cash_account(cash_gateway, type_name=petty_cash.name)

    for bank_gateway in ManualTransferGateway.objects.all():
        get_cash_account(bank_gateway, type_name=bank_cash.name)

    account_receivable, _ = get_or_create_type(parent=asset, name=names["ACCOUNT_RECEIVABLE"])
    account_receivable.save()

    liabilities, _ = get_or_create_type(name=names["LIABILITY"])
    liabilities.debit = AccountType.DECREASE
    liabilities.save()

    account_payable, _ = get_or_create_type(parent=liabilities, name=names["ACCOUNT_PAYABLE"])
    account_payable.debit = AccountType.DECREASE
    account_payable.save()

    partner_balance, _ = get_or_create_type(parent=liabilities, name=names["PARTNER_BALANCE"])
    partner_balance.debit = AccountType.DECREASE
    partner_balance.save()

    # for partner in Partner.objects.all():
    #     get_partner_payable_account(partner)
    #     get_partner_receivable_account(partner)

    revenue, _ = get_or_create_type(name=names["REVENUE"])
    revenue.debit = AccountType.DECREASE
    revenue.save()

    expenses, _ = get_or_create_type(name=names["EXPENSE"])
    expenses.save()

    # Invoke Hooked Account Initialization
    funcs = hookup.get_hooks("REGISTER_INITIAL_ACCOUNTS")
    for func in funcs:
        func()
