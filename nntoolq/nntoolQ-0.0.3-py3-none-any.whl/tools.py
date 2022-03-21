# coding=utf-8

from .util import send_mail_util
from .util import json_util


class Tool(object):
    def __init__(self):
        self.mail_from_user = ''  # 邮件发送者账号
        self.mail_from_user_pwd = ''  # 邮件发送者密码
        self.mail_from_host = ''  # 邮件发送host

    def send_mail_msg(self, to_user, subject, content):
        send_mail_util(self.mail_from_user, self.mail_from_user_pwd, self.mail_from_host, to_user, subject, content)

    @staticmethod
    def json_loads(json_str):
        return json_util(json_str, 'json_load', indent=None)

    @staticmethod
    def json_dumps(dict_str, **kwargs):
        return json_util(dict_str, 'json_dump', **kwargs)
