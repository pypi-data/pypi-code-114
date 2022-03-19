from setuptools import setup,find_packages
setup(
    name="ylq-rich",
    version="0.2",
    author="ylq",
    description="袁力祈，何慧华",
    packages = find_packages("ylq"), # 模块的保存目录
    package_dir = {"":"ylq"}, # 告诉 setuptools 包都在 ckh 下
    package_data = {
        "":[".txt",".info","*.properties",".py"],
        "":["data/*.*"],
    },
    exclude = ["*.test","*.test.*","test.*","test"]
)