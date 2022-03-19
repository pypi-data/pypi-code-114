from setuptools import setup,find_packages
setup(
    name="Lwenxuan",
    version="0.1",
    description="shenjiayi-yeyuqian",
    author="sjy,yyq",
    packages = find_packages("sjy"),
    package_dir = {"":"sjy"},

    package_data = {
      "":[".txt",".info","*.properties",".py"],
# 包含 data 文件夹下所有的 *.dat 文件
      "":["data/*.*"],
    },
# 取消所有测试包
    exclude = ["*.test","*.test.*","test.*","test"]
)
