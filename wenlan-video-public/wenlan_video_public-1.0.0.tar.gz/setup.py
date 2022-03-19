#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: Haoyu Lu
# Mail: lhy1998@ruc.edu.cn
# Created Time:  2022-3-18 19:17:34
#############################################

import os
 
with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as readme:
    README = readme.read()
 
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
 
# setuptools.setup(
#     name="example-pkg-YOUR-USERNAME-HERE", # 库名，需要在pypi中唯一
#     version="0.0.1",                       # 版本号
#     author="Example Author",               # 作者
#     author_email="author@example.com",     # 作者邮箱（方便使用者发现问题后联系我们）
#     description="A small example package", # 简介
#     long_description=long_description,              # 详细描述（一般会写在README.md中）
#     long_description_content_type="text/markdown",  # README.md中描述的语法（一般为markdown）
#     url="https://github.com/pypa/sampleproject",   # 库/项目主页，一般我们把项目托管在GitHub，放该项目的GitHub地址即可
#     packages=setuptools.find_packages(),    #默认值即可，这个是方便以后我们给库拓展新功能的
#     classifiers=[                    # 指定该库依赖的Python版本、license、操作系统之类的
#         "Programming Language :: Python :: 3",
#         "License :: OSI Approved :: MIT License",
#         "Operating System :: OS Independent",
#     ],
#     install_requires=[               # 该库需要的依赖库
#         '你的库依赖的第三方库（也可以指定版本）',
#         # exapmle
#         'pyautogui',
#         'Django >= 1.11, != 1.11.1, <= 2',
#     ],
#     python_requires='>=3.6',
# )

from setuptools import setup, find_packages            #这个包没有的可以pip一下

setup(
    name = "wenlan_video_public",      #这里是pip项目发布的名称
    version = "1.0.0",  #版本号，数值大的会优先被pip
    keywords = ("pip", "wenlan"),
    description = "Wenlan - Large scale cross-modal pre-training model",
    long_description = "A large-scale video-language pre-training model.",
    license = "MIT Licence",

    url = "https://github.com/rucmlcv/Wenlan-Video-Public",     #项目相关文件地址，一般是github
    author = "Haoyu Lu",
    author_email = "lhy1998@ruc.edu.cn",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["numpy"],        #这个项目需要的第三方库

    classifiers=[                   
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)