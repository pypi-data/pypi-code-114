#coding:utf-8

import yagmail
import json
import requests

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
        return data
    elif isinstance(data, str):
        data = json.loads(data)
        print("成功转换为dict格式")
        return data
    else:
        print("请输入json或dict数据")
        return data


def Url_Sp(url,data:dict):
    """
     url拼接
    :param url:
    :param data:
    :return:
    """
    P_ter = ''
    for k,v in data.items():
        E_nt = f"{k}={v}"
        P_ter = P_ter+'&'+E_nt
    url = url + '?' + P_ter
    url = url.replace("&", "", 1)
    print('拼接成功',url)
    return url

def http_request(type,url,**kwargs):
    """
    """
    if type == 'post':
        rq = requests.post(url,kwargs)
    elif type == 'get':
        rq = requests.get(url,kwargs)
    elif type == 'delete':
        rq = requests.delete(url)
    elif type == 'options':
        rq = requests.options(url)
    elif type == 'head':
        rq = requests.head(url)
    elif type == 'patch':
        rq = requests.patch(url)
    else:
        rq = requests.put(url)
    # print(f"{type}")
    # print(rq.status_code)
    print(rq.text)
    return rq


if __name__ == '__main__':
    # Url_Sp('htts://www.baidu.com',{'a':1,'b':'B','c':'12c'})
    # import requests
    url = 'https://www.baidu.com/'
    # url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send'
    type = 'post'
    myobj = {'key': '7fdda192-cfcb-4eb5-87a5-b341574562d5'}

    http_request(type, Url_Sp(url, myobj))



