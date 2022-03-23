#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/2/1 15:20
# @Author : 心蓝
import re

from .common.db_handler import DB
from .common.log_handler import get_logger
from .case import BaseCase


class TestProducer:

    def __init__(self, data):
        self.data = data

    def produce(self):

        project = {
            'name': self.data.get('name', 'easytest'),
            'host': self.data.get('host'),
            'db_config': self.data.get('db_config'),
            'interfaces': self.data.get('interfaces')
        }
        BaseCase.project = project

        BaseCase.logger = self.logger

        db_handler = self.__get_db_handler()

        BaseCase.db = db_handler

        test_suits = []

        for index, test_suit in enumerate(self.data['test_suits']):
            class_name = 'TestSuit{:05}'.format(index)
            _class = type(class_name, (BaseCase, ), test_suit)

            test_suits.append(_class)
        return test_suits

    def __get_db_handler(self):
        """
        连接数据库
        :param :
        :return:
        """
        if self.data.get('db_config'):
            return DB(**self.data['db_config'])


