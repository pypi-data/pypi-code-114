#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

readme = """
# calc20

#### 介绍
生成60道20以内减法的运算习题

#### 软件架构
Python 3.7.7


#### 安装教程

1.  xxxx
2.  xxxx
3.  xxxx

#### 使用说明

1.  xxxx
2.  xxxx
3.  xxxx

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
"""
# with open('README.md') as readme_file:
    # readme = readme_file.read()

history = ""
# with open('HISTORY.md') as history_file:
    # history = history_file.read()

requirements = [
    'et-xmlfile==1.1.0',
    'openpyxl==3.0.9',
]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    version='0.0.5',
    author="Yarving Liu",
    author_email='yarving@qq.com',
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="生成60道20以内数字减法运算题",
    entry_points={
        'console_scripts': [
            'calc20=calc20.main:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='calc20',
    name='calc20',
    packages=find_packages(
        include=['calc20', 'calc20.*']
    ),
    setup_requires=setup_requirements,
    exclude_package_data={'': ["*.xlsx"]},
    zip_safe=False,
)
