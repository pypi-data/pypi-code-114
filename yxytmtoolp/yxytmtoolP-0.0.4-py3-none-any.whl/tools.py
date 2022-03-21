# @Time    : 2022/3/15 7:15 下午 
# @Author  : yangxy
# @File    : tools.py 
# @Desc    :
# @Software: PyCharm

from .util import send_mail_util
from .util import json_util

class Tool(object):
    def __init__(self):
        self.mail_from_user = ''  # 邮件发送者账号
        self.mail_from_user_pwd = '' # 邮件发送者密码
        self.mail_from_user_host = '' # 邮件发送者host
        # self.qy_wechat_token = '' # 企业微信机器人token

    def send_mail_msg(self, to_user, subject, content):
        send_mail_util(self.mail_from_user, self.mail_from_user_pwd, self.mail_from_user_host, to_user, subject, content)

    def json_loads(json_str):
        return json_util(json_str, 'json_load', indent=None)

    def json_dumps(dict_str, **kwargs):
        return json_util(dict_str, 'json_dump', **kwargs)