from fastapi import Header

from .redis import RedisUtils
from .my_jwt import my_jwt

class AuthConfig(object):
    """
    RedisConfig Redis配置类
    :version: 1.2
    :date: 2020-02-11
    """

    SECRET_KEY = ""


async def get_auth_data(authorization: str = Header(None)):
    """
    获取登录用户认证数据, 通常用于controller层
    :param authorization: 请求header中的authorization
    :return:
    """
    return get_auth_data_by_authorization(authorization)


def get_auth_data_by_authorization(authorization: str, ex: int = None):
    """
    获取登录用户认证数据
    :param authorization:
    :param prefix: 前缀
    :param ex: 数据过期秒数
    :return:
    """
    if authorization:
        return get_auth_data_by_token(authorization, ex)

    return None


def get_auth_data_by_token(token: str, ex: int = None):
    """
    获取登录用户认证数据， 从redis中读取
    :param token: 登录的token
    :param ex: 数据过期秒数
    :return: 登录认证数据
    """
    
    payload = {}
    my_jwt1 = my_jwt()

    try:
        payload, msg = my_jwt1.validate_token(token)
    except Exception as err_info:
        print("controller ERROR:",err_info)
        pass

    return payload

#鉴权
def auth_pr():
    print("鉴权")


def update_auth_data(auth_data: dict, ex: int = None):
    """
    更新认证数据
    :param auth_data: 登录认证数据
    :param ex: 数据过期秒数
    """
    RedisUtils().set('token:' + auth_data.get('token'), auth_data, ex)
