# coding:utf-8
'''
@File    : tools.py
@Author  : chendb
@Desc    : 工具类
'''



from .util import send_mail_util, json_util, send_robot_msg_util, time_stamp_util, get_now_time_util, random_string_util


class Tool(object):

    def __init__(self):
        self.mail_from_user = ''        # 邮件发送者账号
        self.mail_from_user_pwd = ''    # 邮件发送者密码
        self.mail_from_user_host = ''   # 邮件发送者host
        self.qy_wechat_token = ''       # 企业微信机器人token


    def send_mail_msg(self, to_user, subject, content):
        # 发送邮件
        send_mail_util(self.mail_from_user, self.mail_from_user_pwd, self.mail_from_user_host, to_user, subject, content)

    @staticmethod
    def json_loads(json_str):
        # dict -> str
        return json_util(json_str, 'json_load', indent=None)

    @staticmethod
    def json_dumps(dict_str, **kwargs):
        # str -> dict
        return json_util(dict_str, 'json_dump', **kwargs)
    
    def send_qy_wechat_msg(self, msg, at_all=None):
        # 发送企微机器人webhook
        if at_all is None:
            at_all = []
        send_robot_msg_util(msg, 'qyWechat', qy_wechat_token=self.qy_wechat_token, at_all=at_all)
    
    @staticmethod
    def time_stamp(time_stamp='s'):
        # 当前时间戳
        return time_stamp_util(time_stamp)
    
    @staticmethod
    def get_now_time(date_type='-'):
        return get_now_time_util(date_type, 'now')
    
    @staticmethod
    def time_stamp_to_date(time_stamp, date_type='-'):
        # 时间戳转日期
        return get_now_time_util(date_type, time_stamp)
    
    @staticmethod
    def date_to_time_stamp(time_stamp, date_type='-'):
        # 日期转时间戳
        return get_now_time_util(date_type, time_stamp, True)
    