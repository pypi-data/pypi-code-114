import setuptools
from WeiXinNativePay.version import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="WeiXinNativePay",
    version=__version__,
    author="navysummer",
    author_email="navysummer@yeah.net",
    description="WeiXinNativePay是基于微信Native支付开发的sdk",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitee.com/navysummer/WeiXinNativePay",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        # "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
    platforms='python',
    install_requires=[
    ]

)

"""
1、打包流程
打包过程中也可以多增加一些额外的操作，减少上传中的错误

# 先升级打包工具
pip install --upgrade setuptools wheel twine

# 打包
python setup.py sdist bdist_wheel

# 检查
twine check dist/*

# 上传pypi
twine upload dist/*
# 安装最新的版本测试
pip install -U lesscode-py -i https://pypi.org/simple
"""
