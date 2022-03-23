# -*- coding: utf-8 -*-
# python 3.x
# author：huangxiaoyan
# data:"2021/7/22 16:14"
from datetime import datetime

import requests
import urllib3

from base.logger import Log

logger = Log('RequestsHandle')


def time_account(httpRequest):
    def wrapper(self, *args, **kwargs):
        since = datetime.now()
        result = httpRequest(self, *args, **kwargs)
        time_elapsed = datetime.now() - since
        logger.info("耗时{}".format(time_elapsed))
        return result
    return wrapper


class RequestsHandle:
    def __init__(self):
        """session管理器"""
        requests.adapters.DEFAULT_RETRIES = 5
        self.session = requests.session()
        self.session.keep_alive = False

    @time_account
    def httpRequest(self, method, url, params=None, data=None, json=None, headers=None):
        urllib3.disable_warnings()
        proxies = {"http": None, "https": None}
        if not isinstance(data, dict) and data is not None:
            data = data.encode('utf-8').decode("latin1")
        result = self.session.request(method, url, params=params, data=data, json=json, headers=headers, verify=False,
                                      proxies=proxies)
        try:
            result = result.json()
        except:
            pass
        self.close_session()
        return result

    def close_session(self):
        self.session.close()

