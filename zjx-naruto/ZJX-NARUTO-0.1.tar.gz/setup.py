# 通过 setuptools 模块导入所需要的函数
from setuptools import setup,find_packages
setup(
    name="ZJX-NARUTO",
    version="0.1",
    author="郑俊贤",
    packages = find_packages("ZJX"),
    package_dir = {"":"ZJX"},
    package_data = {
        "":[".txt",".info","*.properties",".py"],
        "":["data/*.*"],
    },
    exclude = ["*.test","*.test.*","test.*","test"]
)