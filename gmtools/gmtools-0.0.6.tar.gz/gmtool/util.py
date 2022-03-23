# coding:utf-8
'''
@File    : util.py
@Author  : guomin
@Desc    : 工具方法
'''

import yagmail
import urllib.parse
import requests
import json

def send_mail_util(from_user,pwd,host,to_user,subject,content):
    """
    :param from_user:发件人
    :param pwd:发件人密码
    :param host:发件主机
    :param to_user:接收人
    :param subject:邮件主题
    :param content:邮件内容
    :return :
    """

    try:
        with yagmail.SMTP(user=from_user,password=pwd,host=host) as yag:
            yag.send(to_user,subject,content)
    except Exception as e:
        print("发生错误:{}".format(e))

def json_util(data):
    """
    字符串转字典或者字典转字符串
    :param data:待转换的数据
    :return
    """
    if type(data)==str and data.startswith("{") and data.endswith("}"):
        return eval(data)
    elif type(data)==dict:
        return str(data)
    else:
        print( "数据不适用!!")

def join_url_util(url,data):
    """
    :param url:url路径
    :param data:待拼接参数
    """
    if type(data)==dict:
        query_string=urllib.parse.urlencode(data)
    else:
        print("数据非字典格式")
    return url+"?"+query_string

def http_request_util(method,url,body,headers=None):
    """
    :param method:请求方法
    :param url:请求地址
    :param data:请求数据
    :param headers:请求头
    :return
    """
    try:
        r=requests.request(method=method,url=url,data=json.dumps(body),headers=headers)
        return r.text
    except Exception as e:
        print("发生错误:{}".format(e))
    


# 验证方法
if __name__=="__main__":
    # send_mail_util("tech-tm-qa@pin-dao.cn","Tm-qa-888888","smtp.mxhichina.com","guomin1@pin-dao.cn","主题","你好呀内容")
    # data='{"key":1,"key2":"1256463","key3":"8923hfds"}'
    # print(type(json_util(data)))
    # print(join_url("https://qyapi.weixin.qq.com/cgi-bin/webhook/send",{"key":"7fdda192-cfcb-4eb5-87a5-b341574562d5"}))
    body={ "params": {"username": "13821910557","password": "tc123456"},"type": 0}
    # print(type(json_util(body)))
    # print(type(json.dumps(body)))
    headers={"Content-Type": "application/json"}
    # print(http_request_util("post","https://operate-api.pin-dao.cn/teacore/login",body,headers=headers))