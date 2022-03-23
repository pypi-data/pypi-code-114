from setuptools import setup,find_packages
setup(
    name="gmy",
    version="0.3",
    author="gmy",
    description="高梦瑶   谭茜文",
    packages = find_packages("gmy"), # 模块的保存目录
    package_dir = {"":"gmy"}, # 告诉 setuptools 包都在 ckh 下
    package_data = {
        "":[".txt",".info","*.properties",".py"],
        # 包含 data 文件夹下所有的 *.dat 文件
        "":["data/*.*"],
    },

    exclude = ["*.test","*.test.*","test.*","test"]
)

