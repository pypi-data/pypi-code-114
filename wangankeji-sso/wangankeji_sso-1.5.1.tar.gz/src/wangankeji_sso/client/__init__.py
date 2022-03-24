import logging

from .client import SsoClient
from .enums import SsoErrorCodes, SsoCommands
from .exceptions import SsoException
from .http import SsoRequest, ResponseToSso, AbstractSsoRequestHandler, ResponseFromSso
from .models import SsoOption, SsoDataHeader, SsoToken

logger = logging.getLogger('sso')


class Sso:
    def __init__(self, option: SsoOption, request_handler: AbstractSsoRequestHandler):
        self.option = option
        self.request_handler: AbstractSsoRequestHandler = request_handler
        """
        请求处理器
        """

        self.client = SsoClient(option.app_id, option.sso_url)
        self.client.set_keys(option.sso_public_key, option.app_private_key)

    def accept(self, environ: dict, data: (str, bytes)) -> ResponseToSso:
        """

        :param environ:
        :param data:
        :return:
        """
        request_path = environ.get('PATH_INFO')
        logger.info('收到来自 %s的SSO请求: %s' % (environ.get('REMOTE_ADDR'), request_path))
        method = environ.get('REQUEST_METHOD').lower()

        sso_request = SsoRequest(request_path, environ, data)
        sso_request.set_keys(self.option.sso_public_key, self.option.app_private_key)
        try:
            sso_request.resolve_data()
        except SsoException as ex:
            logger.error("解析请求数据出错", exc_info=ex)

        sso_response = ResponseToSso(sso_request)
        sso_response.set_keys(self.option.sso_public_key, self.option.app_private_key)

        if sso_request.exception:
            exception = sso_request.exception
            if isinstance(exception, SsoException):
                sso_response.error_code = exception.code
            else:
                sso_response.error_code = SsoErrorCodes.UNKNOWN_SSO_ERROR
        else:
            # 校验APPID
            if sso_request.header.app_id != self.option.app_id:
                sso_response.error_code = SsoErrorCodes.HEADER_APPID_INVALID
            else:
                if method == 'get':
                    self.request_handler.get(sso_request, sso_response)
                elif method == 'post':
                    self.request_handler.post(sso_request, sso_response)
                elif method == 'delete':
                    self.request_handler.delete(sso_request, sso_response)
                else:
                    logger.warning('不支持的方法: ' + method)
                    sso_response.error_code = SsoErrorCodes.HEADER_METHOD_UNSUPPORTED

        return sso_response.get_response()


__all__ = [
    'Sso',
    'AbstractSsoRequestHandler',
    'SsoOption',
    'SsoRequest',
    'SsoErrorCodes',
    'SsoCommands',
    'SsoException',
    'ResponseToSso',
    'ResponseFromSso',
    'SsoDataHeader',
    'SsoToken'
]
