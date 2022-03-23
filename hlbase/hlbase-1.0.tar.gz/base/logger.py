# -*- coding: utf-8 -*-
# python 3.x
# author：huangxiaoyan
# data:"2021/7/20 10:47"

import logging
import time
import os

from common import logPath


class Log:
    def __init__(self, name='root'):
        self.name = name
        self.log_path = logPath
        if not os.path.exists(logPath):
            os.makedirs(logPath)

    def my_log(self, level, msg):
        loger = logging.getLogger(self.name)
        loger.setLevel(logging.DEBUG)
        # loger.propagate = False  # 关闭系统控制台输出
        formatter = logging.Formatter('%(asctime)s-[%(levelname)s]-%(filename)s-%(name)s-日志信息:%(message)s')

        sh = logging.StreamHandler()
        sh.setLevel(logging.INFO)
        sh.setFormatter(formatter)

        now = time.strftime('%Y-%m-%d_%H_%M_%S')
        new_log_path = os.path.join(self.log_path + os.sep + "Api_Autotest_log_{0}.log".format(now[0:10]))
        fh = logging.FileHandler(new_log_path, 'a', encoding='utf-8')
        fh.setLevel(logging.INFO)
        fh.setFormatter(formatter)

        loger.addHandler(sh)
        loger.addHandler(fh)

        if level == 'debug':
            loger.debug(msg)  # 根据level输出日志级别
        elif level == 'info':
            loger.info(msg)
        elif level == 'error':
            loger.error(msg)
        elif level == 'warning':
            loger.warning(msg)

        loger.removeHandler(sh)
        loger.removeHandler(fh)

    def debug(self, msg):
        self.my_log('debug', msg)

    def info(self, msg):
        self.my_log('info', msg)

    def error(self, msg):
        self.my_log('error', msg)

    def warning(self, msg):
        self.my_log('warning', msg)
