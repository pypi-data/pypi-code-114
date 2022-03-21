from setuptools import setup,find_packages
setup(
    name="cb-handsome",
    version="0.1",
    author="cb",
    description="组长：方俊龙，组员：陈彪，组员：叶文龙",
    packages = find_packages("cb"), # 模块的保存目录
    package_dir = {"":"cb"}, # 告诉 setuptools 包都在 ckh 下
    package_data = {
    "":[".txt",".info","*.properties",".py"],
    "":["data/*.*"],
    },
    exclude = ["*.test","*.test.*","test.*","test"]
)
