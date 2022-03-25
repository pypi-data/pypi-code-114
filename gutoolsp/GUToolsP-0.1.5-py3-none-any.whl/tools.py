#coding:utf-8

from .util import send_mail_util, json_util, Url_Sp, http_request

class Tool(object):
    def __init__(self):
        self.mail_from_user = ''  # 邮件发送者账号
        self.mail_from_user_pwd = ''  # 邮件发送者密码
        self.mail_from_host = ''  # 邮件发送host

    def send_mail_msg(self, to_user, subject, content):
        send_mail_util(self.mail_from_user, self.mail_from_user_pwd, self.mail_from_host, to_user, subject, content)
    
    def json_change(self, data):
        return json_util(data)

    def url_sp(self, url, data):
        return Url_Sp(url, data)
        
    def http_request(self, type, url, **kwargs):
        return http_request(type, url, **kwargs)








