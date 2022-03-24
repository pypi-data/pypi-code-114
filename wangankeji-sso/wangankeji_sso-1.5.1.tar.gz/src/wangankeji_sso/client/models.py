import logging

from .enums import SsoCommands, SsoErrorCodes
from .exceptions import SsoException

logger = logging.getLogger('sso')


class SsoOption:
    def __init__(self):
        self.app_id = ''
        """
        应用的 AppId
        """
        self.app_private_key = ''
        """
        应用RSA密钥对的私钥
        """
        self.sso_public_key = ''
        """
        SSO密钥对的公钥
        """
        self.sso_url = ''
        """
        SSO 接口地址
        """

    @classmethod
    def load_dir(cls, dir_name: str):
        """
        从目录加载配置
        结构为:
        APP私钥: app_private_key.pem
        SSO公钥: sso_public_key.pem
        配置项: option.ini
        :param dir_name: 配置存放的目录
        :return: SsoOption实例
        """

        import os
        sso_pub_key = cls._read_file(os.path.join(dir_name, 'sso_public_key.pem'))
        app_priv_key = cls._read_file(os.path.join(dir_name, 'app_private_key.pem'))
        sso_url, app_id = cls._load_config(os.path.join(dir_name, 'option.ini'))

        options = SsoOption()
        options.app_id = app_id
        options.sso_url = sso_url
        options.sso_public_key = sso_pub_key
        options.app_private_key = app_priv_key
        return options

    @staticmethod
    def _read_file(name):
        with open(name) as fp:
            return fp.read()

    @staticmethod
    def _load_config(name):
        from configparser import ConfigParser
        parser = ConfigParser()
        parser.read(name, encoding='utf8')
        url = parser.get('wangankeji_sso', 'sso_url')
        appid = parser.get('wangankeji_sso', 'app_id')

        return url, appid


class SsoDataHeader:
    """
    请求或响应头信息
    """

    def __init__(self):
        # X-COMMAND 请求的命令字
        self.command = SsoCommands.UNKNOWN
        # X-TOKEN 请求或响应的TOKEN，由SSO生成
        self.token = None
        # X-CODE 错误码
        self.code = SsoErrorCodes.NONE
        # X-KEY 本次使用AES加密TOKEN时的KEY(IV)，此数据通过RSA加密后传输
        self.key = ''
        # X-APPID 应用的标识，仅在应用向SSO发起请求或响应SSO请求时才需要此项。
        # 在应用接入成功时，会将此值发送给应用，
        # 应用也可以在任何时间通过命令字Commands.AppID来获取
        self.app_id = ''

    def __str__(self):
        return '<SsoDataHeader APPID=%s, COMMAND=%s, CODE=%s>' % (self.app_id, self.command, self.code)

    def to_dict(self):
        """
        将数据头处理成字典格式
        :return:
        """
        return {
            'command': self.command.value,
            'code': self.code.value,
            'appid': self.app_id,
            'key': self.key,
            'token': None if self.token is None else str(self.token)
        }

    @staticmethod
    def parse(meta: str or int):
        """
        将HTTP头信息处理成 SsoDataHeader
        :param meta:
        :return:
        """
        header = SsoDataHeader()
        command = SsoDataHeader._get_item(meta, 'COMMAND')
        if not command:
            logger.warning('数据缺少 command 头')
            raise SsoException(SsoErrorCodes.HEADER_COMMAND_MISSING)

        cmd = SsoCommands.parse(command)
        header.command = cmd

        if cmd == SsoCommands.UNKNOWN:
            logger.warning('无效的 command 值:' + command)
            raise SsoException(SsoErrorCodes.HEADER_COMMAND_INVALID)

        code = SsoDataHeader._get_item(meta, 'CODE')
        header.code = SsoErrorCodes.parse(code)

        app_id = SsoDataHeader._get_item(meta, 'APPID')
        if not app_id:
            logger.warning('缺少参数 appid')
            raise SsoException(SsoErrorCodes.HEADER_APPID_MISSING)

        header.app_id = app_id
        header.key = SsoDataHeader._get_item(meta, 'KEY')
        header.token = SsoDataHeader._get_item(meta, 'TOKEN')

        return header

    @staticmethod
    def _get_item(meta: dict, key: str):
        """
        从 request.META 读取一个值
        :param meta:
        :param key:
        :return:  如果值不存在会返回 None
        """
        # 处理格式
        key_fmt1 = "HTTP_X_%s" % key
        key_fmt2 = "X-%s" % key
        for (k, v) in meta.items():
            if k.upper() == key_fmt1 or k.upper() == key_fmt2:
                return v

        return None


class SsoToken:
    """
    传输Token
    数据格式: TOKEN-ID|应用内用户ID|应用内角色ID|SSO用户ID|SSO用户名|SSO用角色ID|SSO用户角色|附加数据
    """

    def __init__(self):
        # 值为时间戳，单位为秒，不包含毫秒部分
        self.id = -1
        # 应用内用户ID
        self.app_uid = ''
        # 应用内用户角色ID
        self.app_rid = ''
        # SSO用户ID
        self.sso_uid = -1
        # SSO用户名
        self.sso_uname = ''
        # SSO用角色ID
        self.sso_rid = -1
        # SSO用角色名
        self.sso_rname = ''
        # 附加数据
        self.data = ''

    def __eq__(self, other):
        if other is None:
            return False

        return (
                       self.id == other.id or self.id == other.data or self.data == other.id
               ) and (
                       self.sso_uid == other.sso_uid and self.sso_rid == other.sso_rid
               ) and (
                       self.app_uid == other.app_uid and self.app_rid == other.app_rid
               )

    def __str__(self):
        return '|'.join([
            str(self.id),
            str(self.app_uid),
            str(self.app_rid),
            str(self.sso_uid),
            self.sso_uname,
            str(self.sso_rid),
            self.sso_rname,
            str(self.data)
        ])

    def __repr__(self):
        return '<SsoToken id=%s, app_uid=%s, app_rid=%s, sso_uid=%s, sso_uname=%s, sso_rid=%s, sso_rname=%s, data=%s>' % (
            str(self.id),
            str(self.app_uid),
            str(self.app_rid),
            str(self.sso_uid),
            self.sso_uname,
            str(self.sso_rid),
            self.sso_rname,
            str(self.data)
        )

    @staticmethod
    def parse(data: str):
        """
        将字符串数据处理成 SsoToken 结构
        :param data:
        :return:
        """
        if not data:
            return None

        token = SsoToken()
        [
            token.id,
            token.app_uid,
            token.app_rid,
            token.sso_uid,
            token.sso_uname,
            token.sso_rid,
            token.sso_rname,
            token.data
        ] = data.split('|')

        return token


class SsoAppKey:
    """
    APP 相关的密钥数据
    """

    def __init__(self):
        self.sso_public_key = None
        self.sso_pri_key = None
        self.app_public_key = None


class OpenAppResult:
    def __init__(self):
        self.error_code = SsoErrorCodes.NONE
        """
        错误码
        """
        self.token = ''
        """
        成功时的 Token 串
        """
        self.do_login_url = ''
        """
        应用注册时填写用于登录的接口地址
        """
        self.login_url = ''
        """
        应用注册时填写登录失败后的跳转地址（登录页）
        """
        self.main_url = ''
        """
        应用注册时填写登录成功后的跳转地址（主页）
        """

    def __str__(self):
        if self.error_code != SsoErrorCodes.NONE:
            return '<OpenAppResult error=%s>' % str(self.error_code)

        return '<OpenAppResult token=%s>' % str(self.token)
