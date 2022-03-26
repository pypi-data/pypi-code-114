__all__ = ('OrderPoint',)

from expressmoney.api import *


SERVICE = 'scoring'


class OrderCreateContract(Contract):
    order_id = serializers.IntegerField(min_value=1)


class OrderReadContract(Contract):
    pagination = PaginationContract()
    id = serializers.IntegerField(min_value=1)
    created = serializers.DateTimeField()
    score = serializers.DecimalField(max_digits=3, decimal_places=2)
    order_id = serializers.IntegerField(min_value=1)


class OrderID(ID):
    _service = SERVICE
    _app = 'credit_scoring'
    _view_set = 'order'


class OrderPoint(ListPointMixin, CreatePointMixin, ContractPoint):
    _point_id = OrderID()
    _read_contract = OrderReadContract
    _create_contract = OrderCreateContract
