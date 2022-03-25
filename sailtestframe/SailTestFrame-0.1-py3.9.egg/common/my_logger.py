# @Time : 2022/3/16 11:23 PM 
# @Author : SailYang


import logging
import sys
from logging.handlers import TimedRotatingFileHandler

from concurrent_log_handler import ConcurrentRotatingFileHandler

# 设置日志的名称
LOGGER_NAME = 'main'
# 指定日志的等级必须在 LOG_LEVEL变量里
LOG_LEVEL = ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG']


# 创建一个日志对象
class MyLogger(object):
    def __init__(self, logger_name=LOGGER_NAME,
                 log_level: LOG_LEVEL = None,
                 file_name=None,
                 file_size=512 * 1024,
                 log_format="%(asctime)s - %(name)s - %(levelname)s %(process)d - %(processName)s"
                            " - %(thread)s - %(threadName)s - %(message)s"):
        """
        支持控制台和文件输出的日志对象
        """
        self.log_level = log_level

        # 设置日志格式
        self.formatter = logging.Formatter(log_format)

        # 指定 log 文件
        self.filename = file_name

        # 指定 log 文件大小
        self.file_size = file_size

        # 指定 logger 名称
        self.logger_name = LOGGER_NAME

        self.logger = logging.getLogger(logger_name)

        # 设置日志等级
        try:
            self.logger.setLevel(logging.DEBUG if not self.log_level else self.log_level)
        except Exception:
            self.logger.error("Log 等级必须等于 LOG_LEVEL")
            raise ValueError('Log 等级必须等于 LOG_LEVEL')

        # 为日志对象添加流的处理器 handler
        self.logger.addHandler(self.get_console_handler())

        # 为日志对象添加文件处理器 handler
        if file_name:
            self.logger.addHandler(self.get_file_handler())

        self.propagate = False

    def get_logger(self, module_name):
        """
        对子日志对象的支持
        """
        return logging.getLogger(self.logger_name).getChild(module_name)

    def get_console_handler(self):
        # 创建一个流处理器 handler
        # StreamHandler默认参数是 sys.stderr 即异常信息，对应的输入信息为 sys.stdin，输出为 sys.stdout
        ch = logging.StreamHandler(sys.stdout)

        # 创建一个日志格式器 formatter 并将其添加到处理器 handler
        ch.setFormatter(self.formatter)

        # 每次没调用后清空已存在的 handler
        self.logger.handlers.clear()
        return ch

    def get_file_handler(self):
        # 创建一个文件流的处理器
        # ConcurrentRotatingFileHandler 可以在多进程环境下安全地将日志写入同一个文件
        # 并且可以在日志达到特定大小时，按照文件大小分割日志，但不支持按时间分割日志
        fh = ConcurrentRotatingFileHandler(self.filename, "a", self.file_size, encoding="utf-8")
        fh.setFormatter(self.formatter)
        return fh

    def info(self, msg, extra=None):
        self.logger.info(msg, extra=extra)

    def error(self, msg, extra=None):
        self.logger.error(msg, extra=extra)

    def debug(self, msg, extra=None):
        self.logger.debug(msg, extra=extra)

    def warning(self, msg, extra=None):
        self.logger.warning(msg, extra=extra)
