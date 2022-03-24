import logging
from enum import unique, IntEnum

from .exceptions import SsoException

logger = logging.getLogger('sso')


@unique
class SsoCommands(IntEnum):
    """
    接口命令字
    """

    # 未知命令
    UNKNOWN = 0
    # 回放数据，用于连接测试等
    ECHO = 1
    # 角色信息操作
    USER = 2,
    # 绑定用户
    ROLE = 3,
    # 登录
    BIND = 4,
    # 登录
    LOGIN = 5
    # 退出
    LOGOUT = 6
    # 打开 APP
    OPEN_APP = 7

    @staticmethod
    def parse(value):
        if value is None:
            return SsoCommands.UNKNOWN
        # noinspection PyBroadException
        try:
            return SsoCommands(int(value))
        except Exception:
            logger.exception('Parse command failed')
            return SsoCommands.UNKNOWN


@unique
class SsoErrorCodes(IntEnum):
    """
    错误码表
    """
    # 未发生错误
    NONE = 0x0000

    # SSO发生未知错误
    UNKNOWN_SSO_ERROR = 0x0001
    # 请求头中未包含X-APPID
    HEADER_APPID_MISSING = 0x0101
    # 请求头中未包含X-COMMAND
    HEADER_COMMAND_MISSING = 0x0102
    # 请求头中未包含X-TOKEN
    HEADER_TOKEN_MISSING = 0x0103
    # 请求体不为空时，未包含X-KEY头
    HEADER_KEY_MISSING = 0x0104
    # 不支持的请求方法METHOD
    HEADER_METHOD_UNSUPPORTED = 0x0105
    # X-COMMAND无效
    HEADER_COMMAND_INVALID = 0x0106
    # 请求方法METHOD不支持此命令 X-COMMAND
    HEADER_COMMAND_UNSUPPORTED = 0x0107
    # 请求中包含的token无效
    HEADER_TOKEN_INVALID = 0x0108
    # 请求中的token已过期
    HEADER_TOKEN_EXPIRED = 0x0109
    # 从X-KEY解密出IV失败
    HEADER_KEY_DECRYPTED_FAILED = 0x010A
    # 请求体为空
    BODY_EMPTY = 0x010B
    # 请求体无效，出现在解码失败时
    BODY_INVALID = 0x010C
    # body请求体需要列表
    BODY_IS_NOT_LIST = 0x010D
    # body请求体需要字典(对象)
    BODY_IS_NOT_DICT = 0x010E
    # 请求头中未包含X-CODE
    HEADER_CODE_MISSING = 0x010F
    # 请求头中X-CODE无效
    HEADER_CODE_INVALID = 0x0110
    # 请求头中X-APPID无效
    HEADER_APPID_INVALID = 0x0111
    # SSO 用户未登录
    SSO_NOT_LOGIN = 0x0112

    # 应用不存在
    APP_NOT_EXISTS = 0x0201
    # 用户未登录
    USER_IS_OFFLINE = 0x0202

    # 应用用户不存在
    USER_NOT_EXISTS = 0x0301
    # 用户未绑定
    USER_NOT_BOUND = 0x0302
    # 用户已禁用
    USER_DISABLED = 0x0303

    # 应用角色不存在
    ROLE_NOT_EXISTS = 0x0401

    # 通过解密出来的IV去解密数据失败
    IV_INVALID = 0x0501
    # RSA解密数据体失败
    BODY_DECRYPT_FAILED = 0x0502
    # 用户名或密码无效
    INVALID_USER_OR_PSWD = 0x0601

    # 请求失败(status code != 200)
    RESPONSE_STATUS_UNEXPECTED = 0x0701

    @staticmethod
    def parse(value):
        if value is None:
            return SsoErrorCodes.NONE
        # noinspection PyBroadException
        try:
            return SsoErrorCodes(int(value))
        except Exception:
            logger.exception('Parse code failed')
            raise SsoException(SsoErrorCodes.HEADER_CODE_INVALID)
