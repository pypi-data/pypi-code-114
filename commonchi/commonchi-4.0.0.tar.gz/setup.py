#!/usr/bin/env python
#-*- coding:utf-8 -*-

from setuptools import setup, find_packages
from codecs import open
from os import path
import os
here = path.abspath(path.dirname(__file__))
#依赖文件
#requirement=open('requirements.txt').readline() 




setup(
    name='commonchi',
    version='4.0.0',
    description='commonchi',
    #long_description=str(open(path.join(here, "README.md")).read()),
    # The project's main homepage.
    url='',
    # Author details
    author='cxx',
    author_email='cuixiaoxia@chinasofti.com',
    # Choose your license
    license='',

	py_modules=["commonchi.lib.api","commonchi.lib.Context","commonchi.lib.newReport","commonchi.lib.public","commonchi.lib.readexcel","commonchi.lib.ReplaceVariable","commonchi.lib.sendmail","commonchi.lib.sendrequests","commonchi.lib.writeexcel","commonchi.lib.utility","commonchi.package.HTMLTestRunner"],
	install_requires=["Appium-Python-Client==0.48",
	"bleach==4.1.0",
	"certifi==2021.5.30",
	"charset-normalizer==2.0.4",
	"colorama==0.4.4",
	"configparser==5.0.0",
	"DateTime==4.4",
	"ddt==1.3.1",
	"distlib==0.3.4",
	"document==1.0",
	"docutils==0.18.1",
	"et-xmlfile==1.0.1",
	"filelock==3.4.1",
	"idna==3.2",
	"importlib-metadata==4.8.3",
	"importlib-resources==5.4.0",
	"jdcal==1.4.1",
	"Jinja2==3.0.1",
	"keyring==23.4.1",
	"lxml==4.7.1",
	"MarkupSafe==2.0.1",
	"meteo-downloader==1.0",
	"multi-key-dict==2.0.3",
	"multitasking==0.0.10",
	"nose==1.3.7",
	"nose-html-reporting==0.2.3",
	"numpy==1.19.5",
	"openpyxl==3.0.2",
	"packaging==21.3",
	"pandas==0.25.3",
	"pbr==5.8.1",
	"pkginfo==1.8.2",
	"platformdirs==2.4.0",
	"Pygments==2.11.2",
	"PyMySQL==1.0.2",
	"pyparsing==3.0.7",
	"python-dateutil==2.8.2",
	"pytz==2021.3",
	"pywin32-ctypes==0.2.0",
	"qiniu==7.5.0",
	"readme-renderer==32.0",
	"requests==2.26.0",
	"requests-toolbelt==0.9.1",
	"rfc3986==1.5.0",
	#"selenium==3.14.0",
	"six==1.16.0",
	"tqdm==4.62.3",
	"typing_extensions==4.1.1",
	"upload==0.1.1",
	"urllib3==1.26.8",
	"virtualenv==20.13.1",
	"webencodings==0.5.1",
	"xlrd==1.2.0",
	"xlutils==2.0.0",
	"xlwt==1.3.0",
	"yfinance==0.1.70",
	"zipp==3.6.0",
	"zope.interface==5.4.0"
],  
)
#安装依赖：install_requires





#  setup.py各参数介绍：
#
# --name 包名称
#
# --version (-V) 包版本
#
# --author 程序的作者
#
# --author_email 程序的作者的邮箱地址
#
# --maintainer 维护者
#
# --maintainer_email 维护者的邮箱地址
#
# --url 程序的官网地址
#
# --license 程序的授权信息
#
# --description 程序的简单描述
#
# --long_description 程序的详细描述
#
# --platforms 程序适用的软件平台列表
#
# --classifiers 程序的所属分类列表
#
# --keywords 程序的关键字列表
#
# --packages 需要处理的包目录（包含__init__.py的文件夹）
#
# --py_modules 需要打包的python文件列表
# --download_url 程序的下载地址
#
# --cmdclass
#
# --data_files 打包时需要打包的数据文件，如图片，配置文件等
#
# --scripts 安装时需要执行的脚步列表
#
# --package_dir 告诉setuptools哪些目录下的文件被映射到哪个源码包。一个例子：package_dir = {'': 'lib'}，表示“root package”中的模块都在lib 目录中。
#
# --requires 定义依赖哪些模块
#
# --provides定义可以为哪些模块提供依赖
#
# --find_packages() 对于简单工程来说，手动增加packages参数很容易，刚刚我们用到了这个函数，它默认在和setup.py同一目录下搜索各个含有 __init__.py的包。