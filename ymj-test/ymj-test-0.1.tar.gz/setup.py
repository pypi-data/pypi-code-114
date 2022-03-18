from setuptools import setup,find_packages 
setup(
    name="ymj-test", 
    version="0.1", 
    author="ymj", 
    description="i am ymj from gzist",
    packages = find_packages("sohandsome"), # 模块的保存目录 
    package_dir = {"":"sohandsome"}, # 告诉 setuptools 包都在 ckh 下 
    package_data = { 
    # 定义打包除了 .py 之外的文件类型，此处 .py 其实可以不写
    "":[".txt",".info","*.properties",".py"], 
    # 包含 data 文件夹下所有的 *.dat 文件 
    "":["data/*.*"], },
    # 取消所有测试包 
    exclude = ["*.test","*.test.*","test.*","test"] 
)