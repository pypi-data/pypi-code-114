#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup

from backlog import __author__, __license__, __title__, __version__

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name=__title__,  # ライブラリの名前（PyPIにこの名前で登録される）
    version=__version__,  # バージョン（二重管理防止のため＿init＿.pyから読込む事が望ましい）
    author=__author__,  # 作者名
    # author_email='49798519+ryobs@users.noreply.github.com',  # 作者のEメールアドレス
    maintainer=__author__,  # 管理者（個人開発なら作者と同じ）
    # maintainer_email='ryo8000@users',  # 管理者のEメールアドレス
    url="https://github.com/ryo8000/backlog-api4py",  # URL（GitHubのURLを登録することが多い）
    # download_url="https://github.com/ryo8000/backlog-api4py",
    # ダウンロードURL（GitHubのURLを登録することが多い）
    description="Backlog API for Python",  # ライブラリの簡単な説明
    long_description=readme,  # ライブラリの詳細説明。READMEを登録するとPyPIのトップ画面に表示される
    license=__license__,  # ライセンス
    packages=[  # パッケージ構成（複数登録することも可能）
        "backlog", "backlog.models",
    ],
    python_requires=">=3.7.0",  # Pythonのバージョン要件
    install_requires=[  # 必須パッケージ
        "requests>=2.0"
    ],
    # extras_require=,  # 推奨パッケージ
    # tests_require=[],
    # cmdclass={},
    classifiers=[  # 各種分類情報
        "Topic :: Software Development",  # タグ（表示順に注意）
        "Development Status :: 7 - Inactive",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Intended Audience :: Developers",
    ]
)
