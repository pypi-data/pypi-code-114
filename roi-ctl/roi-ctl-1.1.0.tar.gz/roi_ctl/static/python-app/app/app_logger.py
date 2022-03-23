#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from .app_static import get_logger_file

import logging

# 日期格式
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
# 日志格式
BASIC_FORMAT = '[%(asctime)s][%(threadName)s][%(levelname)s][ %(filename)s:%(lineno)s] : %(message)s '
# 日期内容格式
LOG_FORMAT = logging.Formatter(BASIC_FORMAT, DATE_FORMAT)
LOG_FILE = get_logger_file()

LOG_CONSOLE_HANDLER = logging.StreamHandler()
LOG_FILE_HANDLER = logging.FileHandler(LOG_FILE, 'a', encoding='utf-8')


class AppLogger():
    """
    LOG 
    """
    def __init__(self):
        # 日志对象
        self.logger = logging.getLogger("CAPTURE")
        # 日志文件
        LOG_FILE_HANDLER.setFormatter(LOG_FORMAT)
        LOG_FILE_HANDLER.setLevel(logging.INFO)
        self.logger.removeHandler(LOG_FILE_HANDLER)
        self.logger.addHandler(LOG_FILE_HANDLER)


logger = AppLogger().logger

