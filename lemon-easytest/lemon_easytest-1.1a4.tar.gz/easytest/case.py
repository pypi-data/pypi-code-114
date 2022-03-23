#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/2/1 15:21
# @Author : 心蓝
"""Test case implementation"""
import re
import json
from unittest import TestCase

import requests
from jsonpath import jsonpath
from faker import Faker

from .common.log_handler import MyLoggerHandler
# from .common.log_handler import logger


class BaseCase(TestCase):
    name = None   # 功能名称
    db = None
    # logger = logger  # 日志器

    def add_log_handler(self):
        if self.logger:
            for h in self.logger.handlers:
                self.logger.removeHandler(h)
            self.logs = getattr(self, 'logs', [])
            new_handler = MyLoggerHandler(self.logs)
            new_handler.setLevel(self.logger.parent.handlers[0].level)
            new_handler.setFormatter(self.logger.parent.handlers[0].formatter)
            self.logger.addHandler(new_handler)

    @classmethod
    def setUpClass(cls) -> None:
        pass
        # 类前置
        # cls.logger.info('=========={}测试开始============'.format(cls.name))
        # print('==========注册接口测试开始============')

    @classmethod
    def tearDownClass(cls) -> None:
        pass
        # 类后置
        # cls.logger.info('=========={}测试结束============'.format(cls.name))
        # print('==========注册接口测试结束============')

    @classmethod
    def send_http_request(cls, url, method='get', **kwargs) -> requests.Response:
        """
        sent http request
        :param url: 
        :param method: 
        :param kwargs: 
        :return: 
        """
        if getattr(cls, 'session', None) is None:
            cls.session = requests.session()
        method = method.lower()
        return getattr(cls.session, method)(url, **kwargs)

    def flow(self, testcase):
        self.add_log_handler()
        self.case = testcase
        self._test_name = '测试套件【{}】用例【{}】:'.format(self.__class__.name, self._testMethodName)
        self.logger.debug('{}开始测试>>>>>>>>'.format(self._test_name))
        try:
            self.__process_test_data()

            self.send_request()

            self.__assert_res()

            # self.__extract_data_from_response()
            self.logger.info('{}测试成功<<<<<<<<<'.format(self._test_name))
        except Exception as e:
            self.logger.warning('{}测试失败<<<<<<<<<'.format(self._test_name))
            self.logger.exception(e)
            raise e
        finally:
            self.logger.debug('{}测试结束<<<<<<<<<'.format(self._test_name))

    def __process_test_data(self):
        """
        处理测试数据
        :return:
        """
        self.generate_test_data()
        self.__check_case()
        self.__replace_args()
        self.__process_url()
        self.__handle_request_data()

    def generate_test_data(self):
        """
        动态生成测试数据 phone
        :return:
        """
        fake = Faker('zh-cn')
        fake_keys = dir(fake)
        # 子类可以复写实现自定义的生成测试数据
        # 1 生成动态数据并替换
        temp = json.dumps(self.case)
        keys = re.findall(r'\$(\w*?)\$', temp)
        for key in keys:
            if key not in fake_keys:
                self.logger.error('${}$这个动态数据关键字不支持'.format(key))
                raise ValueError('${}$这个动态数据关键字不支持'.format(key))
            value = str(getattr(fake, key)())
            temp = temp.replace('${}$'.format(key), value)
        self.case = json.loads(temp)

    def __check_case(self):
        """
        检查用例数据格式
        :return:
        """
        keys = ['title', 'method', 'url', 'status_code']
        for key in keys:
            if key not in self.case:
                raise ValueError('用例数据错误！必须包含【{}】字段'.format(key))

    def __process_url(self):
        """
        处理url
        :return:
        """
        if self.case['url'].startswith('http'):
            pass
        elif self.case['url'].startswith('/'):
            self.case['url'] = self.settings.get('host') + self.case['url']
        else:
            if self.case['url'] not in self.settings.get('interfaces'):
                self.logger.warning('{}处理url错误：接口名字 \'{}\'不正确'.format(self._test_name, self.case['url']))
                raise ValueError('{}处理url错误：接口名字 \'{}\'不正确'.format(self._test_name, self.case['url']))
            self.case['url'] = self.settings.get('host') + self.settings.get('interfaces')[self.case['url']]

    def __replace_args(self):
        """
        替换参数
        """
        temp = json.dumps(self.case)
        temp = self.replace_args_by_re(temp)
        self.case = json.loads(temp)

    def __handle_request_data(self):
        """
        处理请求数据
        :return:
        """
        if self.case.get('request'):
            self.case['request'] = self.__loads_by_json_or_eval(self.case['request'])
        else:
            self.case['request'] = {}

    def send_request(self):
        """
        发送请求，当有特殊处理时可以复写
        """
        try:
            self.response = self.send_http_request(url=self.case['url'], method=self.case['method'],
                                                   **self.case['request'])
        except Exception as e:
            self.logger.warning('{}发送http请求错误: {}'.format(self._test_name, e))
            self.logger.warning('url:{}'.format(self.case['url']))
            self.logger.warning('method:{}'.format(self.case['method']))
            self.logger.warning('args:{}'.format(self.case['request']))
            raise RuntimeError('{}发送http请求错误:{}'.format(self._test_name, e))

    def __assert_res(self):
        """
        断言
        """
        self.__assert_status_code()
        self.__assert_response()
        self.__extract_data_from_response()
        self.__assert_db()

    def __assert_status_code(self):
        """
        响应状态码断言
        :return:
        """
        try:
            self.assertEqual(self.case['status_code'], self.response.status_code)
        except AssertionError as e:
            self.logger.warning('{}状态码断言失败！'.format(self._test_name))
            try:
                self.response.text
            except:
                pass
            else:
                self.logger.warning('响应数据为:{}'.format(self.response.text))
            raise e
        else:
            self.logger.debug('{}状态码断言成功！'.format(self._test_name))
            self.get_response_data()

    def get_response_data(self):
        if self.case.get('res_type') is None:
            self.logger.debug('注意：没有设置res_type，只有响应体为空的时候有用')
            return
        if self.case['res_type'].lower() == 'json':
            self.response_data = self.response.json()
        elif self.case['res_type'].lower() == 'xml':
            self.response_data = self.response.text
        elif self.case['res_type'].lower() == 'html':
            self.response_data = self.response.text
        else:
            raise ValueError('{}响应数据提取错误：请指定合适的响应类型,支持的类型有json,xml,html'.format(self._test_name))

    @property
    def assert_funcs(self):
        return {
                    'eq': self.assertEqual,
                    'neq': self.assertNotEqual,
                    'gt': self.assertGreater,
                    'gte': self.assertGreaterEqual,
                    'lt': self.assertLess,
                    'lte': self.assertLessEqual,
                    'in': self.assertIn,
                    'nin': self.assertNotIn
                }

    def __assert_response(self):
        if self.case.get('assertion'):
            self.__check_assertion_field()
            if not self.case.get('assertion'):
                return
            for item in self.case['assertion']:
                actual_res = self.__extract_data_by_express(item[2])
                expect_res = item[0]
                assert_func = self.assert_funcs.get(item[1])
                if assert_func is None:
                    self.logger.error('不支持操作符【{}】'.format(item[1]))
                    raise ValueError('不支持操作符【{}】'.format(item[1]))
                try:
                    assert_func(expect_res, actual_res)
                except Exception as e:
                    self.logger.warning('{}响应数据断言失败'.format(self._test_name))
                    self.logger.warning('请求数据是: {}'.format(self.case['request']))
                    self.logger.warning('期望结果是：{}'.format(expect_res))
                    self.logger.warning('实际结果是：{}'.format(actual_res))
                    self.logger.warning('校验条件是: {}'.format(item))
                    self.logger.warning('响应回的数据是：{}'.format(self.response_data))
                    raise e
            else:
                self.logger.debug('{}响应数据断言成功'.format(self._test_name))

    def __assert_db(self):
        """
        数据库断言
        :return:
        """
        if not self.case.get('db_assertion'):
            return

        self.case['db_assertion'] = self.replace_args_by_re(self.case['db_assertion'])
        self.case['db_assertion'] = self.__loads_by_json_or_eval(self.case['db_assertion'])
        self.__check_db_assertion_field()

        if not self.case.get('db_assertion'):
            return

        if self.db is None:
            raise RuntimeError('没有数据库链接信息，要数据库断言请填写数据库信息')

        for item in self.case['db_assertion']:
            self.logger.debug('执行sql是: {}'.format(item[2]))
            actual_res = self.db.get_value(item[2])
            expect_res = item[0]

            assert_func = self.assert_funcs.get(item[1])
            if assert_func is None:
                self.logger.error('不支持操作符【{}】'.format(item[1]))
                raise ValueError('不支持操作符【{}】'.format(item[1]))
            try:
                assert_func(expect_res, actual_res)
            except Exception as e:
                self.logger.warning('{}数据库断言失败'.format(self._test_name))
                self.logger.warning('执行sql是: {}'.format(item[1]))
                self.logger.warning('期望结果是：{}'.format(expect_res))
                self.logger.warning('实际结果是：{}'.format(actual_res))
                self.logger.warning('校验条件时: {}'.format(item))
                raise e
        else:
            self.logger.debug('{}数据库断言成功'.format(self._test_name))

    def __loads_by_json_or_eval(self, s):
        """
        将json字符串load为python字典，支持简单的算术表达式，通过eval实现
        :param s:
        :return:
        """
        try:
            if not isinstance(s, str):
                s = json.dumps(s)
            res = json.loads(s)
        except Exception as e:
            try:
                from decimal import Decimal
                res = eval(s)
            except Exception as e:
                self.logger.warning('{}转换json参数失败：{}'.format(self._test_name, e))
                raise ValueError('{}转换json参数失败：{}'.format(self._test_name, e))
            else:
                return res

        else:
            return res

    def replace_args_by_re(self, s):
        """
        通过正则表达式动态替换参数
        :param s: 需要被替换的json字符串
        :return:
        """
        args = re.findall('#(.*?)#', s)
        for arg in set(args):
            value = getattr(self, arg, None)
            if value:
                s = s.replace('#{}#'.format(arg), str(value))
        return s

    def __get_value_from_db(self, condition, sql):
        """
        获取sql对应的值
        :param item:
        :return:
        """
        if condition == 'exist':
            res = self.db.exist(sql)
        elif condition == 'eq':
            res = self.db.get_one_value(sql)
        else:
            raise ValueError('{}数据库断言条件不支持，当前支持：exist,eq'.format(self._test_name))
        return res

    def __extract_data_by_express(self, extract_exp):
        """
        通过表达式提取数据
        """
        if extract_exp.startswith('$'):
            return self.__extract_data_by_jsonpath(extract_exp)
        elif extract_exp.startswith('/'):
            return self.__extract_data_by_xpath(extract_exp)
        else:
            return self.__extract_data_by_re(extract_exp)

    def __extract_data_by_jsonpath(self, extract_exp):
        """
        jsonpath提取数据
        :param obj:
        :param extract_exp:
        :return:
        """
        if self.case.get('res_type') is None or self.case.get('res_type').lower() != 'json':
            res = jsonpath(dict(self.response.headers), extract_exp)
            if res is False:
                raise ValueError('提取请求头的jsonpath表达式错误')
        else:
            res = jsonpath(self.response.json(), extract_exp)
            if res is False:
                res = jsonpath(dict(self.response.headers), extract_exp)
        if res:
            if len(res) == 1:
                return res[0]
            return res

        raise ValueError('{}jsonpath表达式:{}错误'.format(self._test_name, extract_exp))

    def __extract_data_by_xpath(self, extract_exp):
        pass

    def __extract_data_by_re(self, extract_exp):
        res = re.findall(extract_exp, self.response.text)
        if res:
            if len(res) == 1:
                res = res[0]
            return res
        else:
            raise ValueError('正则表达式错误，提取不到值！')

    @staticmethod
    def __extract_data_from_json(obj, extract_exp):
        """
        从json数据里提取数据
        """
        res = jsonpath(obj, extract_exp)
        if not res:
            res = re.findall(extract_exp, json.dumps(obj, ensure_ascii=False))
            if not res:
                return '没有匹配到值'
                # raise ValueError('用例【{}】断言提取表达式:{} 错误'.format(self.case['title'], extract_exp))
        else:
            if len(res) == 1:
                res = res[0]
        return res

    def __extract_actual_res(self, extract_exp):
        if self.case.get('res_type') is None:
            raise ValueError('没有设置res_type')
        if self.case['res_type'].lower() == 'json':
            res = self.response.json()

        if extract_exp[0] == '.':
            keys = extract_exp[1:].split('.')
            for key in keys:
                res = res.get(key)
        return res

    def __extract_data_from_response(self):
        """
        从响应中提取数据
        :return:
        """
        if self.case.get('extract'):

            self.__check_extract_field()
            for item in self.case['extract']:
                value = self.__extract_data_by_express(item[1])
                setattr(self.__class__, item[0], value)

    def __check_extract_field(self):
        """
        检查extract字段格式
        :return:
        """
        self.__check_field('extract', 2)

    def __check_assertion_field(self):
        """
        检查assertion字段格式
        :return:
        """
        self.__check_field('assertion', 3)

    def __check_db_assertion_field(self):
        """
        检查db_assertion字段格式
        :return:
        """
        if isinstance(self.case['db_assertion'], list):
            for item in self.case['db_assertion']:
                if not len(item) == 3:
                    raise ValueError(
                        '{}{}字段格式错误: {} 不是一个{}元列表'.format(self._test_name, 'db_assertion', 3, item))

        else:
            raise ValueError('{0}{1}字段格式错误:{1}字段应该是一个列表'.format(self._test_name, 'db_assertion'))

    def __check_field(self, field_name, length):
        """
        检查field_name字段格式
        :param field_name:
        :param length
        :return:
        """
        try:
            self.case[field_name] = self.__loads_by_json_or_eval(self.case[field_name])
        except Exception as e:
            self.logger.error('{}{}字段json格式错误: {}'.format(self._test_name, field_name, e))
            raise ValueError('{}{}字段json格式错误: {}'.format(self._test_name, field_name, e))

        if isinstance(self.case[field_name], list):
            for item in self.case[field_name]:
                if not len(item) == length:
                    raise ValueError('{}{}字段格式错误: {} 不是一个{}元列表'.format(self._test_name, field_name, item, length))

        else:
            raise ValueError('{0}{1}字段格式错误:{1}字段应该是一个列表'.format(self._test_name, field_name))




