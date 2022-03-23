#!/usr/bin/env python
# -*- encoding: utf-8 -*-


from os.path import dirname, abspath, join, exists

import os
import datetime

"""
必须放到 MODULE_NAME 根路径
"""


def get_static():
    """
    获取静态资源路径
    """
    dirname_root = dirname(dirname(abspath(__file__)))
    return join(dirname_root, "static")


def get_logger_file():
    """
    日志存储文件夹 
    ---
    static/logs/
    """
    dir_static = get_static()
    dir_logger = join(dir_static, "logs")
    if not exists(dir_logger):
        os.makedirs(dir_logger)
    logger_file_name = str(datetime.date.today()).replace("-", "")
    logger_file = join(dir_logger, f"{logger_file_name}.log")
    return logger_file
