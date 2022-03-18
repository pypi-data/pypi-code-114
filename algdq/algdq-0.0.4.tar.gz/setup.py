# -*- coding: gbk-*-
"""
* 作者：王若宇
* 时间：2022/1/25 14:00
* 功能：打包Python软件包用于发布到pypi.org
* 说明：请看读我.txt，库发布后可使用学而思库管理工具下载
"""
import sys

from setuptools import setup,find_packages
#from xes import AIspeak

if __name__ == '__main__':
    sys.argv += ["sdist"]
setup(
    name='algdq',
    version='0.0.4',
    packages=find_packages(),
    url='https://code.xueersi.com/',
    license='MIT License',
    author='algfwq',
    author_email='3104374883@qq.com',
    description='读取库',
    long_description='奥利给读取库',
    requires=[]
)


