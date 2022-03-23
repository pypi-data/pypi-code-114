# -*- coding: utf-8 -*-
# python 3.x
# author：huangxiaoyan
# data:"2022/3/23 15:36"

import os

"""
 用于定义常量
"""
# 获取当前文件路径
current_path = os.path.abspath(__file__)
#  获取当前文件的父目录
# father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
# config.ini文件路径,获取当前目录的父目录的父目录与congig.ini拼接
rootPath = os.path.abspath(os.path.dirname(current_path) + os.path.sep + "..")
# 日志地址
logPath = os.path.join(rootPath, "result", 'log')