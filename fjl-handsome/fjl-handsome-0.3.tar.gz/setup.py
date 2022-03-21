from setuptools import setup,find_packages
setup(
    name="fjl-handsome",
    version="0.3",
    author="方俊龙",
    description="组长：方俊龙，组员：陈彪，叶文龙",
    #url="fjl.handsome.com", 此网站需要存在且未被占用
    packages = find_packages("fjl"), # 模块的保存目录
    package_dir = {"":"fjl"}, # 告诉 setuptools 包都在 ckh 下
    package_data = {
        "":[".txt",".info","*.properties",".py"],
        "":["data/*.*"],
    },
    exclude = ["*.test","*.test.*","test.*","test"]
)

