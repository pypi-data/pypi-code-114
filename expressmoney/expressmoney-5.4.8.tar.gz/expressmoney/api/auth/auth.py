__all__ = ('UserPoint', 'SendPasswordPoint',)

from phonenumber_field.serializerfields import PhoneNumberField

from expressmoney.api import *

SERVICE_NAME = 'auth'


auth_user_send_password = ID(SERVICE_NAME, 'user', 'send_password')
auth_user = ID(SERVICE_NAME, 'user', None)


class UserCreateContract(Contract):
    username = PhoneNumberField()
    ip = serializers.IPAddressField()
    http_referer = serializers.URLField()


class SendPasswordCreateContract(Contract):
    username = PhoneNumberField()


class SendPasswordPoint(CreatePointMixin, ContractPoint):
    _point_id = auth_user_send_password
    _create_contract = SendPasswordCreateContract


class UserPoint(CreatePointMixin, ContractPoint):
    _point_id = auth_user
    _create_contract = UserCreateContract
