# created by virtualenv automatically

"""
* 作者：王若宇
* 时间：2022/1/25 14:00
* 功能：打包Python软件包用于发布到pypi.org
* 说明：请看读我.txt，库发布后可使用学而思库管理工具下载
"""
import sys

from setuptools import setup
from xes import AIspeak

if __name__ == '__main__':
    sys.argv += ["sdist"]
setup(
    name='tkPathBrowser',
    version='1.0.1',
    packages=['tkPathBrowser'],
    url='https://yangguang-gongzuoshi.top/wry/wp',
    license='MIT License',
    author='RuoyuWang',
    author_email='wry_beiyong07@outlook.com',
    description='tkinter路径选择小插件/' + AIspeak.translate('tkinter路径选择小插件'),
    long_description='tkinter路径选择小插按行布可以浏览文件/' + AIspeak.translate('tkinter路径选择小插按行布可以浏览文件'),
    requires=['tkPlus'.replace("p", "P")]
)
