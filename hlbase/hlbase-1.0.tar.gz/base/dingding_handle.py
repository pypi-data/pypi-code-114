# -*- coding: utf-8 -*-
# python 3.x
# author：huangxiaoyan
# data:"2021/8/13 10:29"
import json

from base.request_handle import RequestsHandle
from base.logger import Log

logger = Log('DingdingHandle')


class DingdingHandle(object):
    def set_dingding(self, webhook, data):
        headers = {"Content-Type": "application/json"}
        return RequestsHandle().httpRequest('post', webhook, data=json.dumps(data), headers=headers)
