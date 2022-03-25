#!/usr/bin/python 
# -*- coding: utf-8 -*-

from functools import wraps

__runwell =True
__run_msg = ""

def println(iscontinue=True):
    def decorated(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            __runwell = True
            result = None
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                __runwell =False
                __run_msg = e
                pass
            finally:
                print("{}<Func> execute: {}{}".format(
                                                    func.__name__, 
                                                    result if __runwell else False, 
                                                    ".\t Exception happend: {}".format(__run_msg) if not __runwell else "" ))
                if not iscontinue: exit(0)
            return result
        return wrapper
    return decorated

""" { "suite" : ["测试方法": {"url":"https://XXXX", "data": "json_str", "result": 0+1+2+None} ], 
      "total":10, "passed": 10, , "failed": 0, , "error": 0, "skipped": 0} 
"""
REPORT_DATA = {}

REPORT_DATA["suite"] = []


def test(iscontinue=True):
    def decorated(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            __runwell = True
            result = None
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                __runwell =False
                __run_msg = e
                pass
            finally:
                print("{}<Func> execute: {}{}".format(
                                                    func.__name__, 
                                                    result if __runwell else False, 
                                                    ".\t Exception happend: {}".format(__run_msg) if not __runwell else "" ))
                if not iscontinue: exit(0)
            return result
        return wrapper
    return decorated
