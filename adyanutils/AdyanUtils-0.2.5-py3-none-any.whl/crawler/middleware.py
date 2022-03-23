#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/26 13:54
# @Author  : Adyan
# @File    : middleware.py


import logging
import random
import time

from scrapy.core.downloader.handlers.http11 import TunnelError, TimeoutError
from twisted.internet.error import ConnectionRefusedError
from w3lib.http import basic_auth_header

from Utils import GetProxy


class Proxy(object):

    def __init__(self, settings, spider):
        self.settings = settings
        self.ip_list = []
        try:
            self.proxy = spider.proxy
            if self.proxy.get("name"):
                self.proxies = GetProxy(self.proxy)
        except:
            self.proxy = None

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings, crawler.spider)

    def process_response(self, request, response, spider):
        if request.meta.get("isProxy"):
            start_time = request.meta.get('_start_time', time.time())
            logging.info(
                f'【代理{request.meta["proxy"][8:]}消耗时间{time.time() - start_time}】{request.url}'
            )
            del request.meta["proxy"]
        return response

    def process_request(self, request, spider):
        request.meta.update(
            {
                '_start_time': time.time()
            }
        )

        if self.proxy.get("name"):
            if isinstance(self.ip_list, list):
                if len(self.ip_list) < 5:
                    while True:
                        proxies = self.proxies.get_proxies()
                        if proxies:
                            break
                    self.ip_list = proxies

                request.meta['download_timeout'] = 5
                if request.meta.get("isProxy"):
                    ip_raw = random.choice(self.ip_list)
                    self.ip_list.remove(ip_raw)
                    request.meta["proxy"] = ip_raw
                    request.headers["Connection"] = "close"
            else:
                logging.info('代理列表为空')

        if self.proxy.get("username"):
            request.meta['proxy'] = f"http://{self.proxy.get('proxies')}"
            request.headers['Proxy-Authorization'] = basic_auth_header(
                f'${self.proxy.get("username")}',
                f'${self.proxy.get("password")}'
            )
            request.headers["Connection"] = "close"

    def process_exception(self, request, exception, spider):
        if isinstance(exception, (TunnelError, TimeoutError, ConnectionRefusedError)):
            return request
