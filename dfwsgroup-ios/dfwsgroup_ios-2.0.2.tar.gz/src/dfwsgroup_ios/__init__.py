#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/25 16:46
# @Author  : Lifeng
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm

__version__ = "0.0.1"
__description__ = "ios-稳定测试，记得先在APP上打包 FastbotRunner "

from dfwsgroup_ios.ios.cli import main

__all__ = [
    "__version__",
    "__description__",
    "main",
]
