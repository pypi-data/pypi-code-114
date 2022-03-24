import base64
import json
import logging
from abc import ABC, abstractmethod
from io import StringIO
from typing import List, Optional

import requests
from requests.adapters import HTTPAdapter

from . import utils
from .enums import SsoErrorCodes, SsoCommands
from .exceptions import SsoException
from .models import SsoDataHeader, SsoToken
from .utils import Rsa, Aes

logger = logging.getLogger('sso')


class SsoHttpBase(ABC):
    def __init__(self):
        self.headers = {}
        self.header = SsoDataHeader()
        self.body = None
        self.app_private_key = None
        self.sso_public_key = None
        self.exception = None

    def resolve_data(self):
        header = self.header
        headers = self.headers

        if 'X-CODE' in headers:
            code = int(headers.get('X-CODE'))
            header.code = SsoErrorCodes.parse(code)

        header.command = SsoCommands.UNKNOWN
        if 'X-COMMAND' not in headers:
            logger.warning('缺少 X-COMMAND 头')
            raise SsoException(SsoErrorCodes.HEADER_COMMAND_MISSING)

        command = int(headers.get('X-COMMAND'))
        cmd = SsoCommands.parse(command)
        if cmd == SsoCommands.UNKNOWN:
            logger.warning('无效的 command 值:' + str(command))
            raise SsoException(SsoErrorCodes.HEADER_COMMAND_INVALID)
        header.command = cmd

        if 'X-APPID' not in headers:
            logger.warning('缺少 X-APPID 头')
            raise SsoException(SsoErrorCodes.HEADER_APPID_MISSING)
        header.app_id = headers.get('X-APPID')

        if 'X-TOKEN' in headers:
            token = headers.get('X-TOKEN')
            # 需要使用 RSA 解密
            try:
                header.token = SsoToken.parse(Rsa.decrypt(token, self.app_private_key))
            except Exception as ex:
                logger.error('解密TOKEN失败', exc_info=ex)
                raise SsoException(SsoErrorCodes.HEADER_TOKEN_INVALID)

        if self.body:
            if isinstance(self.body, str):
                body = self.body
            elif isinstance(self.body, bytes):
                body = self.body.decode('utf8')
            else:
                raise SsoException(SsoErrorCodes.BODY_INVALID)

            # 有数据
            # 检查数据头是否正确
            if 'X-KEY' not in headers:
                logger.warning('缺少 X-KEY 头')
                raise SsoException(SsoErrorCodes.HEADER_KEY_MISSING)

            iv = headers.get("X-KEY")
            # 使用 RSA 解
            try:
                header.key = Rsa.decrypt(iv, self.app_private_key)
            except Exception as ex:
                logger.error("解密IV失败", exc_info=ex)
                raise SsoException(SsoErrorCodes.HEADER_KEY_DECRYPTED_FAILED)

            # 解密 因为请求数据必须加密，所以只在这里解析
            try:
                decrypted_ody = Aes.decrypt(body, self.get_aes_key(), header.key)
                self.body = base64.b64decode(decrypted_ody)
            except Exception as ex:
                logger.error("解密BODY失败", exc_info=ex)
                raise SsoException(SsoErrorCodes.BODY_DECRYPT_FAILED)

    def set_keys(self, sso_public_key: str, app_private_key: str):
        """
        设置客户端使用的RSA密钥
        :param sso_public_key:SSO密钥对中的RSA公钥
        :param app_private_key:应用密钥对中的RSA私钥
        :return:
        """
        self.sso_public_key = sso_public_key
        self.app_private_key = app_private_key

    def get_aes_key(self):
        return utils.get_aes_key_from_public_key(self.sso_public_key)


class SsoHttpConnection:
    """
    HTTP连接对象，支持HTTP与HTTPS
    """

    def __init__(self, app_id: str, sso_url: str, entity_id: str, timeout=30, retry=0):
        self.app_id = app_id
        self.sso_url = sso_url
        self.entity_id = entity_id
        self.is_https = sso_url.startswith('https://')
        self.timeout = timeout
        self.retry = retry
        self.headers = {
            'accept': '*/*',
            'connection': 'Keep-Alive',
            'X-APPID': app_id,
        }
        self.method: str = ''
        self.data = None
        self.session = requests.Session()

    @property
    def absolute_uri(self):
        uri = self.sso_url
        if self.entity_id:
            uri += str(self.entity_id)
        return uri

    def set_header(self, name: str, value: any):
        self.headers[name] = str(value)
        logger.info('请求头: %s=%s' % (name, value))

    def write(self, data: str):
        self.data = data

    def send(self) -> requests.Response:
        session = self.session

        session.keep_alive = False
        adapter = HTTPAdapter()
        if self.is_https:
            session.mount('https://', adapter)
        else:
            session.mount('http://', adapter)

        uri = self.absolute_uri

        arguments = {
            'headers': self.headers,
            'verify': False,
            # 'timeout': self.timeout,
            'data': self.data
        }

        method = self.method.lower()

        if method == 'get':
            response = session.get(
                uri, **arguments
            )
        elif method == 'post':
            response = session.post(
                uri, **arguments
            )
        elif method == 'delete':
            response = session.delete(
                uri, **arguments
            )
        else:
            raise SsoException(SsoErrorCodes.HEADER_METHOD_UNSUPPORTED)

        if response.status_code != 200:
            logger.warning(
                'Unexpected response(%s): %s\n%scontent=' % (response.status_code, response.reason, response.text))
            raise SsoException(SsoErrorCodes.RESPONSE_STATUS_UNEXPECTED)

        return response


class SsoRequest(SsoHttpBase):
    """
    收到的SSO请求的对象
    """

    def __init__(self, path_root: str, environ: dict, data: (str, bytes)):
        """
        将请求对象处理成 SsoRequest
        :param path_root: 请求的根路径
        :param environ: wsgi 传递过来的 environ 字典
        :param data: wsgi 传递过来的请求体
        """
        super(SsoRequest, self).__init__()

        self.path = environ.get('PATH_INFO')
        self.headers = self.parse_headers(environ)
        self.body = data
        self.entity_id = self.path[len(path_root):]

    def has_entity_id(self):
        return self.entity_id is not None and self.entity_id != ''

    @classmethod
    def parse_headers(cls, environ: dict):
        headers = {}
        prefix = 'HTTP_X_'
        for key in environ.keys():
            key = key.upper()
            value = environ.get(key)
            if not key.startswith(prefix):
                continue

            key = 'X-' + key[len(prefix):]
            headers[key] = value
        return headers


class ResponseFromSso(SsoHttpBase):
    """
    向SSO发送请求后，SSO的响应对象
    """

    def __init__(self, body: str):
        """

        :param body: SSO返回的响应内容
        """
        super(ResponseFromSso, self).__init__()
        self.body = body


class ResponseToSso(SsoHttpBase):
    """
    收到SSO请求后，返回给SSO的响应对象
    """

    def __init__(self, request: SsoRequest):
        """

        :param request: 经过处理得到的请求体
        """
        super(ResponseToSso, self).__init__()

        self.error_code = SsoErrorCodes.NONE
        self.command: SsoCommands = request.header.command
        self.app_id: str = request.header.app_id
        self.headers = {}
        self.buffer: StringIO = StringIO()

    def write(self, content: str):
        """
        向输出流写数据
        :param content: 要写入输出流的数据
        :return:
        """
        self.buffer.write(content)

    def get_response(self):
        logger.info(
            "响应请求: X-COMMAND=%s, X-CODE=%s, X-APPID=%s" % (self.command.name, self.error_code.name, self.app_id)
        )
        headers = self.headers
        headers.setdefault('Content-Type', 'text/plain')
        headers.setdefault('X-COMMAND', str(self.command.value))
        headers.setdefault('X-CODE', str(self.error_code.value))
        headers.setdefault('X-APPID', self.app_id)

        body = ''

        try:
            if self.buffer.tell():
                # 加密传输的数据
                # 生成一个 iv
                iv = Aes.get_iv()
                encrypted_iv = Rsa.encrypt(iv, self.sso_public_key)
                headers.setdefault('X-KEY', encrypted_iv)
                logger.info("响应数据体不为空，设置响应头 X-KEY=" + encrypted_iv)
                # Base64
                temp = base64.b64encode(self.buffer.getvalue().encode()).decode()
                aes_key = self.get_aes_key()
                body = Aes.encrypt(temp, aes_key, iv)
        finally:
            self.buffer.close()

        logger.info('响应完成')
        return headers, body


class AbstractSsoRequestHandler(ABC):
    """
    处理来自SSO的请求的虚拟实现，用户应该主动实现此类以处理请求
    """

    @abstractmethod
    def get_user(self, user_id: str) -> Optional[dict]:
        """
        获取单个用户信息
        :param user_id:用户ID
        :return:用户对象
        """
        raise NotImplementedError()

    def set_user(self, user: dict):
        """
        设置单个用户信息
        :param user:用户对象
        """
        pass

    def delete_user(self, user_id: str):
        """
        删除单个用户信息
        :param user_id:用户ID
        """
        pass

    @abstractmethod
    def get_all_users(self) -> List[dict]:
        """
        获取所有用户信息
        :return:用户对象列表
        """
        raise NotImplementedError()

    def set_users(self, user: List[dict]):
        """
        设置多个用户信息
        :param user:用户对象集合
        """
        pass

    def delete_users(self, user_ids: list):
        """
        删除多个用户信息
        :param user_ids:用户ID列表
        """
        pass

    @abstractmethod
    def get_role(self, role_id: str) -> Optional[dict]:
        """
        获取单个角色信息
        :param role_id:角色ID
        :return:角色对象
        """
        raise NotImplementedError()

    def set_role(self, role: dict):
        """
        设置单个角色信息
        :param role:角色对象
        """
        pass

    def delete_role(self, role_id: str):
        """
        删除单个角色信息
        :param role_id:角色ID
        """
        pass

    @abstractmethod
    def get_all_roles(self) -> List[dict]:
        """
        获取所有角色信息
        :return:角色对象列表
        """
        raise NotImplementedError()

    def set_roles(self, role: List[dict]):
        """
        设置多个角色信息
        :param role:角色对象集合
        """
        pass

    def delete_roles(self, role_ids: list):
        """
        删除多个角色信息
        :param role_ids:角色ID列表
        """
        pass

    @abstractmethod
    def do_login(self, token: SsoToken) -> SsoErrorCodes:
        """
        根据 SsoToken 信息判断用户是否可以登录
        :param token: 包含用户信息的 SsoToken 对象
        :return: 返回 SsoErrorCodes.None 时表示允许登录
        """
        raise NotImplementedError()

    @abstractmethod
    def do_logout(self, token: SsoToken):
        """
        根据 SsoToken 信息退出登录
        :param token: 包含用户信息的 SsoToken 对象
        """
        raise NotImplementedError()

    @abstractmethod
    def do_bind(self, sso_uid: str, app_uid: str, app_uname: str, password: str) -> SsoErrorCodes:
        """
        绑定应用用户与SSO用户, 需要校验用户密码是否正确
        注: 根据需要存储绑定关系，以处理SSO中多个SSO用户被绑定到同一个应用用户上的问题

        :param sso_uid: 要绑定的SSO用户ID
        :param app_uid: 要绑定的此应用内的用户ID
        :param app_uname: 要绑定的此应用内的用户名
        :param password: 要绑定的此应用内的用户密码
        :return: 返回 SsoErrorCodes.None 时表示允许绑定
        """
        raise NotImplementedError()

    @abstractmethod
    def do_unbind(self, sso_uid: str, app_uid: str, app_uname: str) -> SsoErrorCodes:
        """
        绑定应用用户与SSO用户
        :param sso_uid: 要绑定的SSO用户ID
        :param app_uid: 要绑定的此应用内的用户ID
        :param app_uname: 要绑定的此应用内的用户名
        :return: 返回 SsoErrorCodes.None 时表示允许解除绑定
        """
        raise NotImplementedError()

    def get(self, request: SsoRequest, response: ResponseToSso):
        """
        处理一般(或数据获取)请求
        :param request: SSO请求的对象
        :param response: 响应到SSO的对象
        :return:
        """
        header = request.header

        if request.has_entity_id():
            logger.info('EntityID:' + request.entity_id)

        token = header.token

        if header.command == SsoCommands.USER:
            logger.info('SSO请求获取用户')
            # 获取用户信息
            if request.has_entity_id():
                # 获取单个用户的信息
                try:
                    response.write(json.dumps(self.get_user(request.entity_id)))
                except Exception as ex:
                    logger.error('获取用户信息异常', exc_info=ex)
            else:
                # 获取所有用户的信息
                try:
                    response.write(json.dumps(self.get_all_users()))
                except Exception as ex:
                    logger.error('获取用户信息异常', exc_info=ex)
        elif header.command == SsoCommands.ROLE:
            logger.info('SSO请求获取角色')
            # 获取角色信息
            if request.has_entity_id():
                # 获取单个角色的信息
                try:
                    response.write(json.dumps(self.get_role(request.entity_id)))
                except Exception as ex:
                    logger.error('获取角色信息异常', exc_info=ex)
            else:
                # 获取所有角色的信息
                try:
                    response.write(json.dumps(self.get_all_roles()))
                except Exception as ex:
                    logger.error('获取角色信息异常', exc_info=ex)
        elif header.command == SsoCommands.LOGIN:
            # 用户登录
            logger.info('请求登录 SsoToken=' + str(token))
            response.error_code = self.do_login(token)
        elif header.command == SsoCommands.LOGOUT:
            # 用户退出登录
            logger.info('请求退出登录 SsoToken=' + str(token))
            # 移除应用用户的状态
            self.do_logout(token)
        else:
            response.error_code = SsoErrorCodes.HEADER_COMMAND_UNSUPPORTED

    def post(self, request: SsoRequest, response: ResponseToSso):
        """
        处理数据推送请求
        :param request: SSO请求的对象
        :param response: 响应到SSO的对象
        :return:
        """
        header = request.header

        if request.has_entity_id():
            logger.info('EntityID:' + request.entity_id)

        if header.command == SsoCommands.USER:
            logger.info('SSO请求推送用户')
            # 推送用户信息
            if request.has_entity_id():
                # 推送单个用户的信息
                user = json.loads(request.body)
                self.set_user(user)
            else:
                # 推送所有用户的信息
                users = json.loads(request.body)
                self.set_users(users)
        elif header.command == SsoCommands.ROLE:
            logger.info('SSO请求推送角色')
            # 推送角色信息
            if request.has_entity_id():
                # 推送单个角色的信息
                role = json.loads(request.body)
                self.set_role(role)
            else:
                # 推送所有角色的信息
                roles = json.loads(request.body)
                self.set_roles(roles)
        elif header.command == SsoCommands.BIND:
            # 用户绑定
            logger.info('应用与SSO的用户绑定')
            info = json.loads(request.body)
            sso_uid = info.get('sso_uid')
            app_uid = info.get('app_uid')
            app_uname = info.get('app_uname')
            pswd = info.get('pswd')
            logger.info("SSOUID=%s, APPUID=%s, Name=%s, Password=%s", sso_uid, app_uid, app_uname, pswd)
            response.error_code = self.do_bind(sso_uid, app_uid, app_uname, pswd)
        else:
            response.error_code = SsoErrorCodes.HEADER_COMMAND_UNSUPPORTED

    def delete(self, request: SsoRequest, response: ResponseToSso):
        """
        处理数据删除请求
        :param request: SSO请求的对象
        :param response: 响应到SSO的对象
        :return:
        """
        header = request.header

        if request.has_entity_id():
            logger.info('EntityID:' + request.entity_id)

        if header.command == SsoCommands.USER:
            logger.info('SSO请求删除用户')
            # 删除用户信息
            if request.has_entity_id():
                # 删除单个用户的信息
                self.delete_user(request.entity_id)
            else:
                # 删除所有用户的信息
                user_ids = json.loads(request.body)
                self.delete_users(user_ids)
        elif header.command == SsoCommands.ROLE:
            logger.info('SSO请求删除角色')
            # 删除角色信息
            if request.has_entity_id():
                # 删除单个角色的信息
                self.delete_role(request.entity_id)
            else:
                # 删除所有角色的信息
                role_ids = json.loads(request.body)
                self.delete_roles(role_ids)
        elif header.command == SsoCommands.BIND:
            # 用户解绑
            logger.info('解除应用与SSO的用户绑定')
            info = json.loads(request.body)
            sso_uid = info.get('sso_uid')
            app_uid = info.get('app_uid')
            app_uname = info.get('app_uname')
            logger.info("SSOUID=%s, APPUID=%s, Name=%s", sso_uid, app_uid, app_uname)
            response.error_code = self.do_unbind(sso_uid, app_uid, app_uname)
        else:
            response.error_code = SsoErrorCodes.HEADER_COMMAND_UNSUPPORTED
