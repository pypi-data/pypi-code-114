__all__ = ('BankCardPoint', 'BankCard3dsPoint')

from expressmoney.api import *


SERVICE = 'payments'


class GenericBankCard(Contract):
    bin = serializers.CharField(max_length=6)
    number = serializers.CharField(max_length=4)
    expiry_month = serializers.IntegerField(min_value=1, max_value=12)
    expiry_year = serializers.IntegerField(min_value=2020, max_value=2050)


class BankCardCreateContract(GenericBankCard):
    ip = serializers.IPAddressField(allow_blank=True)
    cryptogram = serializers.CharField(max_length=1024, allow_blank=True)


class BankCardReadContract(GenericBankCard):
    PAYPAL = "PAYPAL"
    CLOUDPAYMENTS = "CLOUDPAYMENTS"
    GATEWAY_CHOICES = (
        (PAYPAL, "PayPal"),
        (CLOUDPAYMENTS, "CloudPayments")
    )
    pagination = PaginationContract()
    id = serializers.IntegerField(min_value=1)
    created = serializers.DateTimeField()
    is_active = serializers.BooleanField()


class BankCard3dsContract(Contract):
    md = serializers.CharField(max_length=512)
    pa_res = serializers.CharField(max_length=512)


class BankCardID(ID):
    _service = SERVICE
    _app = 'bank_cards'
    _view_set = 'bank_card'


class BankCard3dsID(ID):
    _service = SERVICE
    _app = 'bank_cards'
    _view_set = 'bank_card_3ds'


class BankCardPoint(ListPointMixin, CreatePointMixin, ContractPoint):
    _point_id = BankCardID()
    _create_contract = BankCardCreateContract
    _read_contract = BankCardReadContract


class BankCard3dsPoint(CreatePointMixin, ContractPoint):
    _point_id = BankCard3dsID()
    _create_contract = BankCard3dsContract
