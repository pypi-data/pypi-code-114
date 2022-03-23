#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/1/20 19:29
# @Author : 心蓝
import unittest


class TestLoader:
    def __init__(self, data, baseclass):
        self.data = data
        self.baseclass = baseclass

    def loader(self):
        funcs = self._get_test_funcs()
        funcs['settings'] = self.data['settings']
        funcs['logger'] = self.data['logger']
        funcs['db'] = self.data['db']
        testcase_class = type(funcs['name'], (self.baseclass, ), funcs)
        return unittest.defaultTestLoader.loadTestsFromTestCase(testcase_class)

    def _get_test_funcs(self):
        funcs = {}
        for index, item in enumerate(self.data['testcases'], 1):
            func_name = 'test_{:03}_{}'.format(index, item['title'])
            if self.is_marked(item):
                funcs[func_name] = self.wrapper(self.baseclass.flow, item)
            else:
                funcs[func_name] = self.skip_wrapper(self.baseclass.flow, item, self.data['settings'].get('marks', ''))
            funcs[func_name].__doc__ = item['title']
        funcs['name'] = self.data['name']
        return funcs

    def is_marked(self, item):
        marks = self.data['settings'].get('marks', '')
        if marks == '':
            return True

        if set(marks.split(',')) & set((item.get('marks') if item.get('marks') else '').split(',')):
            return True
        return False

    def wrapper(self, func, item):
        #@unittest.skip('test')
        def inner(*args, **kwargs):
            func(testcase=item, *args, **kwargs)
        return inner

    def skip_wrapper(self, func, item, marks):
        @unittest.skip('没有匹配标记:{}'.format(marks))
        def inner(*args, **kwargs):
            func(testcase=item, *args, **kwargs)
        return inner
