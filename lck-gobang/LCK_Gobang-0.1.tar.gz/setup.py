# 通过 setuptools 模块导入所需要的函数
from setuptools import setup,find_packages 
setup(
    name="LCK_Gobang",
    version="0.1",
    author="Lam_ChingKeung",
    url="https://github.com/chuunibyo-kang/simple-gobang", 
    description='python写的简易五子棋，对了，关于组队那个事情，队长是我，队员有张馨和吴泳朗',
    packages = find_packages("lam"), # 模块的保存目录 
    # 告诉 setuptools 包都在 ckh 下 
    package_dir = {"":"lam"}, 
    package_data = {
    # 定义打包除了 .py 之外的文件类型，此处 .py 其实可以不写i
    "":[".txt",".info","*.properties",".py"], # 包含 data 文件夹下所有的 *.dat 文件 "":["data/*.*"],
    },
    # 取消所有测试包
    exclude = ["*.test","*.test.*","test.*","test"]
)