#!/usr/bin/env python
# -*-coding:utf-8 -*-
import configparser as cparser
import datetime
import difflib
import math
import re
import shutil
import time

import os
import zipfile

__author__ = 'jack'

h_time = time.strftime("%H:%M:%S/", time.localtime())
runner = ''


def get_path():
    """
    :return:获取当前工作路径
    """
    return os.getcwd()


def zip_dir(dirname, zipfilename):
    """
    :param dirname: 要打包的文件夹
    :param zipfilename:打包后的zip
    :return:
    """
    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else:
        for root, dirs, files in os.walk(dirname):
            for name in files:
                filelist.append(os.path.join(root, name))
    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(dirname):]
        zf.write(tar, arcname)
    zf.close()


def report_path():
    """
    测试文件存储路径
    :return: report的path
    """
    cf = cparser.ConfigParser()
    cf.read(get_path() + "/config.ini", encoding="utf-8")
    # print(get_path())
    # product_name = cf.get("product_name", "product_name")
    _report_path = dict(cf.items("report"))['path']
    # if not os.path.exists(_report_path):
    #     os.makedirs(_report_path)
    return _report_path


def target_file_path():
    """
    excel测试用例结果文件
    :return: report的path
    """
    cf = cparser.ConfigParser()
    cf.read(get_path() + "/config.ini", encoding="utf-8")
    print(get_path())
    # product_name = cf.get("product_name", "product_name")
    _report_path = dict(cf.items("report"))['path']
    if not os.path.exists(_report_path):
        os.makedirs(_report_path)
    return _report_path


def delete_file(product_name):
    """
    删除文件../report/product_name/
    :return:
    """
    time.sleep(2)
    if os.path.isdir(report_path() + product_name):
        shutil.rmtree(report_path() + product_name)
        time.sleep(2)
    return "ok"


