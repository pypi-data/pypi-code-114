from setuptools import setup,find_packages
setup(
    name="Skyline_Amedazi",
    version="0.1",
    author="Amedazi",
    description="Sole authorized Lord: 李甘雨",
    packages = find_packages("SKA"), # 模块的保存目录
    package_dir = {"":"SKA"}, # 告诉 setuptools 包都在里面
    package_data = {
        "":[".txt",".info","*.properties",".py"],
        # 包含 data 文件夹下所有的 *.dat 文件
        "":["data/*.*"],
    },
    # 取消所有测试包
    exclude = ["*.test","*.test.*","test.*","test"]
)