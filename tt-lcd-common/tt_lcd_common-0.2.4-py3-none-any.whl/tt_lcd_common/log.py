#!/usr/bin/env python

import logging
import sys
import os
from logging.handlers import TimedRotatingFileHandler

DEBUG = 'DEBUG'
INFO = 'INFO'
WARNING = 'WARNING'
ERROR = 'ERROR'
CRITICAL = 'CRITICAL'


def init():
    script_name = sys.argv[0]
    log_folder = os.path.join(os.path.dirname(
        os.path.realpath(__file__)), 'logs')
    script_log_folder = os.path.join(log_folder, script_name)
    log_file = f'{os.path.join(script_log_folder, script_name)}.log'
    return script_name, log_folder, script_log_folder, log_file


class Logger:

    def __init__(self, script_name: str, log_folder: str, script_log_folder: str, log_file: str,
                 main_log_level: str = 'DEBUG', console_log_level: str = 'INFO', file_log_level: str = 'INFO') -> None:
        self.script_name = script_name
        self.log_folder = log_folder
        self.script_log_folder = script_log_folder
        self.log_file = log_file
        self.logger = None
        self.console_handler = None
        self.rotating_file_handler = None
        self.main_log_level = main_log_level
        self.console_log_level = console_log_level
        self.file_log_level = file_log_level
        self.main()

    def create_if_path_not_exist(self, path: str):
        if not os.path.exists(path):
            os.mkdir(path)

    def create_logger(self):
        self.logger = logging.getLogger(self.script_name)
        self.logger.setLevel(self.main_log_level)

    def create_console_handler(self):
        self.console_handler = logging.StreamHandler()
        self.console_handler.setLevel(self.console_log_level)

    def create_rotating_file_handler(self):
        self.rotating_file_handler = TimedRotatingFileHandler(
            self.log_file, when='d', interval=1, backupCount=50)
        self.rotating_file_handler.setLevel(self.file_log_level)

    def set_formatters(self):
        # create formatters
        file_formatter = logging.Formatter(
            '%(levelname)s - %(asctime)s - %(name)s - %(message)s')
        console_formatter = logging.Formatter('%(levelname)s - %(message)s')

        # add formatters to console handler and file handler
        self.console_handler.setFormatter(console_formatter)
        self.rotating_file_handler.setFormatter(file_formatter)

    def add_handlers_to_logger(self):
        self.logger.addHandler(self.console_handler)
        self.logger.addHandler(self.rotating_file_handler)

    def log(self, text: str, log_level: str = 'ERROR'):
        log_level = log_level.upper()
        if log_level == DEBUG:
            self.logger.debug(text)
        elif log_level == INFO:
            self.logger.info(text)
        elif log_level == WARNING:
            self.logger.warning(text)
        elif log_level == ERROR:
            self.logger.error(text)
        elif log_level == CRITICAL:
            self.logger.critical(text)
        else:
            self.logger.error(text)

    def debug(self, text: str):
        self.logger.debug(text)

    def info(self, text: str):
        self.logger.info(text)

    def warning(self, text: str):
        self.logger.warning(text)

    def error(self, text: str):
        self.logger.error(text)

    def critical(self, text: str):
        self.logger.critical(text)

    def main(self):
        self.create_if_path_not_exist(self.log_folder)
        self.create_if_path_not_exist(self.script_log_folder)
        self.create_logger()
        self.create_console_handler()
        self.create_rotating_file_handler()
        self.set_formatters()
        self.add_handlers_to_logger()
