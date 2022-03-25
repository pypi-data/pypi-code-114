# coding:utf-8
'''
@File    : util.py
@Author  : chendb
@Desc    : 工具
'''



import yagmail
import json
import requests
import time
import random
from faker import Faker


def send_mail_util(from_user, pwd, host, to_user, subject, content):
    # 发送邮件
    with yagmail.SMTP(user=from_user, password=pwd, host=host) as yag:
        yag,send(to_user, subject, content)

def json_util(pre_json, to_json_type, **kwargs):
    # json解析
    try:
        return json.loads(pre_json) if to_json_type == 'json_load' else json.dumps(
            pre_json, ensure_ascii=False, **kwargs
        )
    except:
        return pre_json

def trans_data_to_url_util(url, data):
    # 参数拼接转成url形式
    if data:
        url = f'{url}?{"&".join([f"{k}={v}" for k, v in data.items()])}'
    return url

def http_client_util(url, method, data, **kwargs):
    # http请求
    up_method = method.upper()
    if up_method == 'POST':
        res = requests.post(url, data=data, **kwargs)
    elif up_method == 'PUT':
        res = requests.put(url, data=data)
    elif up_method == 'DELETE':
        res = requests.delete(url, data=data, **kwargs)
    elif up_method == 'OPTIONS':
        res = requests.options(url, **kwargs)
    elif up_method == 'HEAD':
        res = requests.head(url, **kwargs)
    elif up_method == 'PATCH':
        res = requests.patch(url, data=data, **kwargs)
    else:
        res = requests.get(url, params=data, **kwargs)
    res.encoding = 'utf-8'
    return res

def send_robot_msg_util(msg, send_type, at_all, qy_wechat_token=''):
    # 机器人webhoook
    payloads = {"msgtype": "text", "text": {"content": msg}}
    if send_type == 'qyWechat':
        payloads['text']['mentioned_mobile_list'] = ['@all'] if at_all is True else at_all
        url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send'
        pre_data = {'key': qy_wechat_token}
        url = trans_data_to_url_util(url, pre_data)
        data = json_util(payloads, 'json_dump').encode('utf-8')
        http_client_util(url, 'POST', data=data, headers={'Content-Type': 'application/json'})

def time_stamp_util(time_type):
    # 时间戳
    t = time.time()
    stamp = int(t * 1000) if time_type == 'ms' else int(t)
    return stamp

def get_now_time_util(format_type, time_stamp, d2s=False):
    # 获取当前时间
    f = '%Y-%m-%d %H:%M:%S' if format_type == '-' else '%Y%m%d%H%M%S'
    if time_stamp == 'now':
        return time.strftime(f, time.localtime())
    elif d2s:
        return int(time.mktime(time.strptime(time_stamp, f)))
    else:
        return time.strftime(f, time.localtime(int(time_stamp)))

def random_string_util(n):
    # 随机字符串
    return ''.join(random.sample(string.ascii_letters + string.digits, n))