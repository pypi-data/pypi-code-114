# @Time    : 2022/3/15 7:15 下午 
# @Author  : yangxy
# @File    : util.py 
# @Desc    :
# @Software: PyCharm

import yagmail
import json

def send_mail_util(from_user, pwd, host, to_user, subject, content):
    """

    :param from_user: 发件人
    :param pwd: 邮箱密码
    :param host: 邮箱host
    :param to_user: 收件人
    :param subject: 主题
    :param content: 内容
    :return:
    """
    with yagmail.SMTP(user=from_user, password=pwd, host=host) as yag:
        yag.send(to_user, subject, content)



def json_util(pre_json, to_json_type, **kwargs):
    """

    :param pre_json: 转换的数据
    :param to_json_type: 转换类型
    :param kwargs:
    :return:
    """
    try:
        if to_json_type == "json_load":
            # print(json.loads(pre_json))
            # print(type(json.loads(pre_json)))
            return json.loads(pre_json)
        else:
            # print(json.dumps(pre_json, ensure_ascii=False,**kwargs))
            # print(type(json.dumps(pre_json, ensure_ascii=False,**kwargs)))
            return json.dumps(pre_json, ensure_ascii=False,**kwargs)
    except:
        return pre_json


# print(json_util(pre_json = '{"age": "12"}', to_json_type = 'json_load'))
# print(json_util(pre_json={'age': '12'}, to_json_type="json_dump"))
# if __name__ == '__main__':
#     # json_util(pre_json={'age': '12'}, to_json_type="json_dump")
#     json_util(pre_json = '{"age": "12"}', to_json_type = 'json_load')


