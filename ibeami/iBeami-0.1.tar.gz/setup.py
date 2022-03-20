from setuptools import setup,find_packages
setup(
    name="iBeami",
    version="0.1",
    author="yyq",
    #url="ckh.handsome.com", 此网站需要存在且未被占用
    packages = find_packages("yyq"), # 模块的保存目录
    package_dir = {"":"yyq"}, # 告诉 setuptools 包都在 yyq 下
    package_data = {
    "":[".txt",".info","*.properties",".py"],
    "":["data/*.*"],
},
    exclude = ["*.test","*.test.*","test.*","test"]
)