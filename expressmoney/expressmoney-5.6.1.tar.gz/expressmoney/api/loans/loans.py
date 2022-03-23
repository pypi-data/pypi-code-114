__all__ = ('LoanPoint', 'LoanPaginationNonePoint', 'PayPoint',)

from typing import OrderedDict, Union

from expressmoney.api import *

SERVICE = 'loans'


class LoanCreateContract(Contract):
    sign = serializers.IntegerField()


class LoanReadContract(LoanCreateContract):
    OPEN = "OPEN"
    OVERDUE = "OVERDUE"
    STOP_INTEREST = "STOP_INTEREST"
    DEFAULT = "DEFAULT"
    CLOSED = "CLOSED"
    STATUS_CHOICES = {
        (OPEN, gettext_lazy("Open loan")),
        (OVERDUE, gettext_lazy("Overdue loan")),
        (STOP_INTEREST, gettext_lazy("Stop interest loan")),
        (DEFAULT, gettext_lazy("Default loan")),
        (CLOSED, gettext_lazy("Closed loan")),
    }
    OPEN_STATUSES = (OPEN, OVERDUE, STOP_INTEREST, DEFAULT)

    pagination = PaginationContract()
    id = serializers.IntegerField(min_value=1)
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()

    amount = serializers.DecimalField(max_digits=7, decimal_places=0, allow_null=True)
    period = serializers.IntegerField()
    expiry_date = serializers.DateField()
    expiry_period = serializers.IntegerField()

    interests_charged_date = serializers.DateField(allow_null=True)
    status = serializers.ChoiceField(choices=STATUS_CHOICES)

    body_balance = serializers.DecimalField(max_digits=7, decimal_places=0, allow_null=True)
    body_paid = serializers.DecimalField(max_digits=7, decimal_places=0, allow_null=True)
    interests_total = serializers.DecimalField(max_digits=7, decimal_places=0, allow_null=True)
    interests_paid = serializers.DecimalField(max_digits=7, decimal_places=0, allow_null=True)
    interests_balance = serializers.DecimalField(max_digits=7, decimal_places=0)

    document = serializers.CharField(max_length=256, allow_blank=True)
    comment = serializers.CharField(max_length=2048, allow_blank=True)


class LoanPaginationNoneReadContract(LoanReadContract):
    pagination = None


class PayUpdateContract(Contract):
    bank_card_id = serializers.IntegerField()


class LoanID(ID):
    _service = SERVICE
    _app = 'loans'
    _view_set = 'loan'


class LoanPaginationNoneID(ID):
    _service = SERVICE
    _app = 'loans'
    _view_set = 'loan'
    _action = 'pagination_none'


class PayID(ID):
    _service = SERVICE
    _app = 'loans'
    _view_set = 'pay'


class LoanPoint(ListPointMixin, CreatePointMixin, ContractPoint):
    _point_id = LoanID()
    _read_contract = LoanReadContract
    _create_contract = LoanCreateContract

    def open_loans(self) -> tuple:
        return self.filter(status=self._read_contract.OPEN_STATUSES)

    def open_loans_last(self) -> Union[None, OrderedDict]:
        objects = self.open_loans()
        return objects[-1] if len(objects) > 0 else None


class LoanPaginationNonePoint(ListPointMixin, ContractPoint):
    _point_id = LoanPaginationNoneID()
    _read_contract = LoanPaginationNoneReadContract


class PayPoint(UpdatePointMixin, ContractObjectPoint):
    _point_id = PayID()
    _update_contract = PayUpdateContract
