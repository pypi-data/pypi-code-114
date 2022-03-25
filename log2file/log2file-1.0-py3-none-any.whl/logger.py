#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import logging.handlers
import time


class flag:
    # 防止多次初始化
    inited = False


def init(logpath="log.log", maxBytes=2 * 1024 * 1024, backupCount=10):
    """
    指定保存日志的文件路径，日志级别，以及调用文件
    将日志存入到指定的文件中
    """
    if flag.inited:
        log = logging.getLogger()
        log.info("already initialized...")

        return

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(filename)s:%(lineno)d - %(message)s")

    # 创建一个handler，用于写入日志文件
    fh = logging.handlers.RotatingFileHandler(logpath, maxBytes=maxBytes, backupCount=backupCount,)
    # fh.setLevel(logging.INFO)
    fh.setLevel(logging.DEBUG)

    # 再创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # 定义handler的输出格式
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # 给logger添加handler
    logging.root.addHandler(ch)
    logging.root.setLevel(logging.DEBUG)

    logging.root.addHandler(fh)
    logging.root.setLevel(logging.DEBUG)

    flag.inited = True


def trace(label=""):
    def handle_func(func):
        def handle_args(*args, **kwargs):
            logging.getLogger(__package__).debug("{1} {0} start...".format(func.__name__, label))
            st = time.time()

            res = func(*args, **kwargs)

            du = time.time() - st
            logging.getLogger(__package__).debug("{1} {0} end cost [{2:0.5}]ms...".format(func.__name__, label, du * 1000))
            return res

        return handle_args

    return handle_func


if __name__ == "__main__":
    init()

    log = logging.getLogger()
    log.error("cc")
