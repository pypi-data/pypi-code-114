# coding:utf-8

from setuptools import setup, find_packages  # 这个包没有的可以pip一下

# 版本信息
version = ''
with open('VERSION', 'r', encoding='utf-8') as file:
    version = file.readline()
    print(version)
# 描述信息
long_description = ""
with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()
    print(long_description)

setup(
    name="pypi_sqlite_cipher",  # 这里是pip项目发布的名称
    version=version,  # 版本号，数值大的会优先被pip
    keywords=["pip", "pypi_sqlite_cipher"],
    description="An feature extraction algorithm",
    long_description=long_description,
    license="MIT Licence",

    url="https://gitee.com/wxb_857_admin/pypi-sqlite-cipher.git",  # 项目相关文件地址，一般是github
    author="XiaoBai",
    author_email="wxok857@foxmail.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=["pytz==2021.1"]  # 这个项目需要的第三方库
)
