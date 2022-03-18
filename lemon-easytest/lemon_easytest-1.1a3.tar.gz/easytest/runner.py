#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/2/1 15:20
# @Author : 心蓝
import time
import threading
import traceback
from multiprocessing.pool import ThreadPool
from unittest.signals import registerResult

from .result import TestResult


class TestRunner:
    resultclass = TestResult

    def run(self, ts):
        result = self._make_result()
        registerResult(result)
        start_time = time.perf_counter()
        startTestRun = getattr(result, 'startTestRun', None)
        if startTestRun is not None:
            startTestRun()
        try:
            ts(result)
        finally:
            stopTestRun = getattr(result, 'stopTestRun', None)
            if stopTestRun is not None:
                stopTestRun()

        stop_time = time.perf_counter()
        duration = stop_time - start_time
        result.duration = duration
        return result

    def _make_result(self):
        return self.resultclass()



class Runner:
    def __init__(self):
        self.result = None
        self.marks = None
        self.thread_num = None
        self.pool = None
        self.lock = None
        self.retry = 0

    def run(self, test_suits):
        self.marks = self.settings.get('marks')
        self.thread_num = self.settings.get('thread_num')
        self.retry = int(self.settings.get('retry', 0))

        if self.marks:
            if isinstance(self.marks, str):
                self.marks = self.marks.split(',')

        self.result = {
            'total_test_suit': len(test_suits),
            'total_test_case': 0,
            'test_suit_result': [],
            'fail_test_case': 0,
            'success_test_case': 0,
            'error_test_case': 0,
            'skip_test_case': 0
        }

        if self.thread_num:
            self.pool = ThreadPool(self.thread_num)
            self.lock = threading.Lock()

            total_s_time = time.time()
            for test_suit in test_suits:
                self.pool.apply_async(self.task, args=(test_suit, ))
            self.pool.close()
            self.pool.join()
        else:
            total_s_time = time.time()
            for test_suit in test_suits:
                self.task(test_suit)
        total_e_time = time.time()
        self.result['duration'] = total_e_time - total_s_time
        if self.result['error_test_case']:
            self.result['status'] = -1
        elif self.result['fail_test_case']:
            self.result['status'] = 1
        else:
            self.result['status'] = 0
        return self.result

    def task(self, test_suit):
        suit_result = {
            'suit_name': test_suit.name,
            'test_case_results': [

            ],
        }
        try:
            test_suit.setUpClass()
            for test_case in test_suit.testcases:
                self.__safe_count_result('total_test_case')
                temp = self.__run_case(test_suit, test_case)
                suit_result['test_case_results'].append(temp)
            test_suit.tearDownClass()
        except Exception as e:
            test_suit.logger.exception(e)
            suit_result['exception'] = traceback.format_exc()
        self.result['test_suit_result'].append(suit_result)

    def __run_case(self, test_suit, test_case):

        temp = {
            'title': test_case['title'],
            # 'case': case
        }
        if self.marks:
            case_mark = test_case.get('marks')
            if not case_mark:
                temp['status'] = 'skipped'
                self.__safe_count_result('skip_test_case')
                return temp
            case_mark = case_mark.split(',')
            if not set(case_mark) & set(self.marks):
                temp['status'] = 'skipped'
                self.__safe_count_result('skip_test_case')
                return temp
        for i in range(self.retry+1):
            if i > 0:
                test_suit.logger.warning('用例【{}】开始第{}次重跑'.format(test_case['title'], i))
            try:
                s_time = time.time()
                test_obj = test_suit()
                test_obj.test(test_case)
                e_time = time.time()
            except AssertionError as e:
                temp['status'] = 'failed'
                temp['exception'] = traceback.format_exc()
                # self.__safe_count_result('fail_test_case')
                test_suit.logger.exception(e)
            except Exception as e:
                temp['status'] = 'broken'
                temp['exception'] = traceback.format_exc()
                # self.__safe_count_result('error_test_case')
                test_suit.logger.exception(e)
            else:
                temp['status'] = 'passed'
                temp['duration'] = (e_time - s_time) * 1000
                self.__safe_count_result('success_test_case')
                break
        if i > 0:
            temp['retry_count'] = i
        temp['case'] = test_obj.case
        if temp['status'] == 'failed':
            self.__safe_count_result('fail_test_case')
        elif temp['status'] == 'broken':
            self.__safe_count_result('error_test_case')

        return temp

    def __safe_count_result(self, key):
        if self.lock:
            self.lock.acquire()
            self.result[key] += 1
            self.lock.release()
        else:
            self.result[key] += 1