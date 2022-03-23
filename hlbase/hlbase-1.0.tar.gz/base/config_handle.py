# -*- coding: utf-8 -*-
# python 3.x
# author：huangxiaoyan
# data:"2021/7/20 10:47"

from configparser import ConfigParser
from base.logger import Log

logger = Log('ConfigHandle')

class ConfigHandle:
    """
      配置文件的封装
    """
    def __init__(self, filename=None):
         self.filename = filename
         self.config = ConfigParser()
         self.config.read(self.filename, encoding='utf-8')


    def get_value(self, section, option):
        """
        字符串类型
        :param section:区域
        :param option:作用域
        :return:
        """
        return self.config.get(section, option)


    def get_int(self, section, option):
        """
        数字类型
        :param section:
        :param option:
        :return:
        """
        return self.config.getint(section, option)


    def get_float(self, section, option):
        """
        浮点数类型
        :param section:
        :param option:
        :return:
        """
        return self.config.getfloat(section, option)


    def get_boolean(self, section, option):
        """
        布尔类型
        :param section:
        :param option:
        :return:
        """
        return self.config.getboolean(section, option)


    def get_eval_data(self, section, option):
        """
        字符串表达式
        :param section:
        :param option:
        :return:
        """

        value = self.get_value(section, option)
        return eval(value)



