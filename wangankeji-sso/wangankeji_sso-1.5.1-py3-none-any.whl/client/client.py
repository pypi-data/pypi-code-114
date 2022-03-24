import base64
import json
import logging
import time
from typing import Optional

from . import utils
from .enums import SsoCommands, SsoErrorCodes
from .exceptions import SsoException
from .http import ResponseFromSso, SsoHttpConnection
from .models import SsoToken, SsoDataHeader, OpenAppResult
from .utils import Rsa, Aes

logger = logging.getLogger('sso')


class SsoClient:
    """
    用户向SSO发送请求的客户端
    """

    def __init__(self, app_id: str, sso_url: str):
        """
        使用指定的应用ID与URL创建客户端实例
        :param app_id:应用ID
        :param sso_url:请求的远程URL
        """
        self.sso_public_key = ''
        self.app_private_key = ''
        self.app_id = app_id
        if sso_url.endswith('/'):
            self.sso_url = sso_url
        else:
            self.sso_url = sso_url + '/'

        logger.info('设置SSO地址:' + self.sso_url)
        self.last_check_login_time = 0
        # True 表示已经登录 False 表示未登录
        self.last_check_login_state = False
        # 是否正在检查
        self.last_check_login_busy = False

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

    def send(self, method: str,
             entity_id: Optional[str],
             command: SsoCommands,
             token: Optional[SsoToken],
             body: str = None) -> ResponseFromSso:
        """
        向SSO发起请求
        :param method: 请求方法，支持: GET, POST, DELETE
        :param entity_id: 要操作数据项的ID，可以为 None
        :param command: 请求的命令
        :param token: 请求的Token信息，与登录状态无关时使用 None
        :param body: 请求数据体，可以为 None
        :return: SSO 响应对象
        """
        header = SsoDataHeader()
        header.command = command

        if token:
            header.token = token

        con = SsoHttpConnection(self.app_id, self.sso_url, entity_id)
        con.method = method

        logger.info('准备向SSO发送请求: %s %s' % (method, con.absolute_uri))

        # 设置请求头
        con.set_header('X-COMMAND', header.command.value)

        if header.token:
            con.set_header('X-TOKEN', Rsa.encrypt(str(header.token), self.sso_public_key))

        if body:
            iv = Aes.get_iv()
            body = Aes.encrypt(base64.b64encode(body.encode()), self.get_aes_key(), iv)
            header.key = Rsa.encrypt(iv, self.sso_public_key)
            con.set_header('X-KEY', header.key)

            con.write(body)

        try:
            logger.info('正在发送请求...')
            # import time
            # s1 = time.perf_counter()
            # logger.info('s1=%s' % str(s1))
            response = con.send()
            # s2 = time.perf_counter()
            # logger.info('s1=%s' % str(s2))
            logger.info('接收响应数据...')

            res = ResponseFromSso(response.text)
            res.set_keys(self.sso_public_key, self.app_private_key)
            res.headers = response.headers
            # s3 = time.perf_counter()
            # logger.info('s1=%s' % str(s3))
            # 准备解析响应数据
            res.resolve_data()
            # s4 = time.perf_counter()
            # logger.info('s1=%s' % str(s4))
            logger.info('响应数据接收完成: %s' % res.header)
            return res
        finally:
            con.session.close()

    def echo(self, data: str) -> ResponseFromSso:
        logger.info('向SSO发送测试连接请求')
        temp = {
            'data': data
        }
        return self.send('POST', None, SsoCommands.ECHO, None, json.dumps(temp))

    def check_login(self, token: SsoToken):
        """
        检查用户的登录状态
        :param token: 当前用户的 token
        :return: 登录状态正常（已经登录，并且未过期/退出)时返回 True, 否则返回 False
        """
        # 如果正在执行状态检查，则返回 true(同时只需要一个检查就行了)
        if self.last_check_login_busy:
            return True
        now = time.time()
        # 如果当前检查登录状态与上次少于 10 秒，则认为仍然处于相同的状态(仅已经登录)
        if now - self.last_check_login_time < 10 and self.last_check_login_state:
            return True

        self.last_check_login_busy = True
        try:
            result = self.send('GET', None, SsoCommands.LOGIN, token)
            self.last_check_login_state = result.header.code == SsoErrorCodes.NONE
        except SsoException as ex:
            logger.warning('检查SSO登录状态错误', exc_info=ex)
            self.last_check_login_state = False
            return False
        finally:
            self.last_check_login_time = now
            self.last_check_login_busy = False

        if not self.last_check_login_state:
            logger.info('检查SSO登录状态错误:' + result.header.code.name)
            return False

        return True

    def logout(self, token: SsoToken):
        """
        退出登录
        :param token:
        :return:
        """
        if not token:
            logger.warning('忽略退出命令：token 为空')
            return
        from .enums import SsoCommands
        self.send('GET', None, SsoCommands.LOGOUT, token)

    def open_app(self, token: SsoToken, app_id: str) -> OpenAppResult:
        """
        使用已经登录的 Token 打开另一个 APP (app_id)
        :param token: 已经登录的 token
        :param app_id: 要打开的 APP ID
        :return: 结果，当 error_code=SsoErrorCodes.NONE 时表示打开成功
        """
        result = self.send('GET', app_id, SsoCommands.OPEN_APP, token)
        oar = OpenAppResult()
        if result.header.code != SsoErrorCodes.NONE:
            oar.error_code = result.header.code
        else:
            data = json.loads(result.body)
            oar.token = data['token']
            oar.do_login_url = data['do_login_url']
            oar.login_url = data['login_url']
            oar.main_url = data['main_url']
        return oar
