#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/26 11:49
# @Author  : Adyan
# @File    : Forge.py


import hashlib
import queue
import re
import threading
import urllib.parse

from faker import Faker
from requests import sessions

fake = Faker()


def hex_md5(cookie, ti, formdata):
    string = f'{re.findall("_m_h5_tk=(.*?)_", cookie)[0]}&{ti}&12574478&{formdata.get("data")}'
    m = hashlib.md5()
    m.update(string.encode('UTF-8'))
    return m.hexdigest()


def url_code(string, code='utf-8'):
    quma = str(string).encode(code)
    bianma = urllib.parse.quote(quma)
    return bianma


def gen_headers(string):
    lsl = []
    headers = {}
    for l in string.split('\n')[1:-1]:
        l = l.split(': ')
        lsl.append(l)
    for x in lsl:
        headers[str(x[0]).strip('    ')] = x[1]

    return headers


class Headers:
    def user_agent(self, mobile_headers):
        while True:
            user_agent = fake.chrome(
                version_from=63, version_to=80,
                build_from=999, build_to=3500
            )
            if "Android" in user_agent or "CriOS" in user_agent:
                if mobile_headers:
                    break
                continue
            else:
                break
        return user_agent

    def header(self, string=None, mobile_headers=None, headers={}):
        if string:
            headers = gen_headers(string)
        headers['user-agent'] = self.user_agent(mobile_headers)
        return headers


class Decode:
    def __init__(self, string):
        pass

    def discern(self):
        pass


def get(args):
    method = args.pop("method")
    url = args.pop("url")
    with sessions.Session() as session:
        return session.request(method=method, url=url, **args)


class ThreadManager(object):
    def __init__(self, work_num: list):
        self.work_queue = queue.Queue()  # 任务队列
        self.threads = []  # 线程池
        self.__work_queue(work_num)  # 初始化任务队列，添加任务
        self.__thread_pool(len(work_num))  # 初始化线程池，创建线程

    def __thread_pool(self, thread_num):
        """
        初始化线程池
        :param thread_num:
        :return:
        """
        for i in range(thread_num):
            # 创建工作线程(线程池中的对象)
            self.threads.append(Work(self.work_queue))

    def __work_queue(self, jobs_num):
        """
        初始化工作队列
        :param jobs_num:
        :return:
        """
        for i in jobs_num:
            #  添加一项工作入队
            self.work_queue.put((get, i))

    def wait_allcomplete(self):
        """
        等待所有线程运行完毕
        :return:
        """
        respone = []
        for item in self.threads:
            item.join()
            respone.append(item.get_result())
        return respone


class Work(threading.Thread):
    def __init__(self, work_queue):
        threading.Thread.__init__(self)
        self.result = None
        self.work_queue = work_queue
        self.start()

    def run(self) -> None:
        # 死循环，从而让创建的线程在一定条件下关闭退出
        while True:
            try:
                do, args = self.work_queue.get(block=False)  # 任务异步出队，Queue内部实现了同步机制
                self.result = do(args)
                self.work_queue.task_done()  # 通知系统任务完成
            except:
                break

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None
