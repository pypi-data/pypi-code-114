__all__ = ('UploadFilePoint', 'UserFilePoint',)

from django.core.validators import RegexValidator

from expressmoney.api import *

SERVICE = 'storage'


class UserFileReadContract(Contract):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z_]*$', 'Only alphanumeric characters are allowed.')

    id = serializers.IntegerField(min_value=1)
    name = serializers.CharField(max_length=64, validators=(alphanumeric,))
    file = serializers.URLField()
    public_url = serializers.URLField(allow_null=True)


class UserFileID(ID):
    _service = SERVICE
    _app = 'storage'
    _view_set = 'user_file'


class UploadFileID(ID):
    _service = SERVICE
    _app = 'storage'
    _view_set = 'upload_file/'


class UserFilePoint(ListPointMixin, ContractPoint):
    _read_contract = UserFileReadContract
    _point_id = UserFileID()
    _app = 'storage'
    _point = 'user_file'


class UploadFilePoint(UploadFilePointMixin, ContractPoint):
    _point_id = UploadFileID()
    _read_contract = None
