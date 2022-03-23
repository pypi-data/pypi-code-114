# -*- coding: utf-8 -*-
# python 3.x
# author：huangxiaoyan
# data:"2022/3/23 15:50"

from distutils.core import setup

setup(
    name="hlbase",
    version=1.0,
    author="huangxiaoyan",
    author_email="469813134@qq.com",
    url='https://pypi.org/manage/projects/',
    packages=['base']
)

# windows py -3 ./base/setup.py sdist
# linux  python setup.py sdist

# twine check ./dist/hlbase-1.0.tar.gz
# twine upload ./dist/hlbase-1.0.tar.gz
# python -m pip install --target=d:\code\helian\my\auto-test\venv\lib\site-packages --upgrade pip

