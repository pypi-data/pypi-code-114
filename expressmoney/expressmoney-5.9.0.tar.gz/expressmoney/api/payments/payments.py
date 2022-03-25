__all__ = ('BankCardPaymentPoint',)

from expressmoney.api import *

SERVICE = 'payments'


class BankCardPaymentCreateContract(Contract):
    LOAN_BODY = 'LOAN_BODY'
    LOAN_INTERESTS = 'LOAN_INTERESTS'
    LOAN_ISSUE = 'LOAN_ISSUE'

    TYPE_CHOICES = {
        (LOAN_BODY, 'Loan body'),
        (LOAN_INTERESTS, 'Loan interests'),
        (LOAN_ISSUE, 'Loan issue'),
    }

    type = serializers.ChoiceField(choices=TYPE_CHOICES)
    amount = serializers.DecimalField(max_digits=16, decimal_places=0, min_value=1, max_value=100000)
    analytical = serializers.IntegerField(min_value=1)
    department = serializers.IntegerField(min_value=1)
    bank_card = serializers.IntegerField(min_value=1)


class BankCardPaymentListContract(BankCardPaymentCreateContract):
    id = serializers.IntegerField(min_value=1)
    created = serializers.DateTimeField()


class BankCardPaymentID(ID):
    _service = SERVICE
    _app = 'payments'
    _view_set = 'bank_card_payment'


class BankCardPaymentPoint(ListPointMixin, CreatePointMixin, ContractPoint):
    _point_id = BankCardPaymentID()
    _create_contract = BankCardPaymentCreateContract
    _read_contract = BankCardPaymentListContract
