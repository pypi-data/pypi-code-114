# 通过 setuptools 模块导入所需要的函数
from setuptools import setup,find_packages
setup(
    name="cfr-real",
    version="0.1",
    author="cfr",
    #url="ckh.handsome.com", 此网站需要存在且未被占用
    description="cfr,dsh,dyl are a group",
    packages = find_packages("cfr"), # 模块的保存目录
    package_dir = {"":"cfr"}, # 告诉 setuptools 包都在 ckh 下
    package_data = {
        # 定义打包除了 .py 之外的文件类型，此处 .py 其实可以不写
        "":[".txt",".info","*.properties",".py"],
        # 包含 data 文件夹下所有的 *.dat 文件
        "":["data/*.*"],
    },
    # 取消所有测试包
    exclude = ["*.test","*.test.*","test.*","test"]
)