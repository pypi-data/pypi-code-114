from django.contrib.contenttypes.models import ContentType

from .models import Account, AccountType
from .settings import journals_setting

names = journals_setting.NAMES


def get_or_create_account(
    name=None,
    type_name=None,
    code=None,
    account_model=None,
    linked_object=None,
):
    filters = dict()
    if account_model is None:
        account_model = Account
    if linked_object is not None:
        ctype = ContentType.objects.get_for_model(linked_object.__class__)
        filters["linked_object_type"] = ctype
        filters["linked_object_id"] = linked_object.id
    if type_name is not None:
        acc_type = AccountType.objects.get(name=type_name)
        filters["account_type"] = acc_type
    filters["code"] = code
    defaults = {"name": name}
    account, created = account_model.objects.get_or_create(**filters, defaults=defaults)
    return account, created


def get_partner_balance_account(partner):
    account, _ = get_or_create_account(
        name="%s (PDM)" % str(partner),
        code="%s.PDM" % partner.inner_id,
        type_name=names["PARTNER_BALANCE"],
        linked_object=partner,
    )
    return account


def get_partner_receivable_account(partner):
    account, _ = get_or_create_account(
        name="%s (PIU)" % str(partner),
        code="%s.PIU" % partner.inner_id,
        type_name=names["ACCOUNT_RECEIVABLE"],
        linked_object=partner,
    )
    return account


def get_cash_account(cash_gateway, type_name=None):
    code = "%s" % cash_gateway.id
    account, _ = get_or_create_account(
        name=str(cash_gateway),
        type_name=type_name or names["CASH"],
        code="CASH.%s" % (code.zfill(4)),
        linked_object=cash_gateway,
    )
    return account
