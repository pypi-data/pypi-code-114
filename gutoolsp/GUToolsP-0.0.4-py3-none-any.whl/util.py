#coding:utf-8

import yagmail
import json

def send_mail_util(from_user, pwd, host, to_user, subject, content):
    """
    发送邮件
    :param from_user: 发件人
    :param pwd: 密码
    :param host: 发送地址host
    :param
    :return:
    """
    with yagmail.SMTP(user=from_user, password=pwd, host=host) as yag:
        yag.send(to_user, subject, content)

def json_util(data):
    """
    格式转换
    :param dict->json
    :param json->dict
    """
    if isinstance(data, dict):
        data = json.dumps(data)
        print("成功转换成json格式")
        return "成功转换成json格式"
    elif isinstance(data, str):
        data = json.loads(data)
        print("成功转换为dict格式")
        return "成功转换为dict格式"
    else:
        print("请输入json或dict数据")
        return"请输入json或dict数据"





    