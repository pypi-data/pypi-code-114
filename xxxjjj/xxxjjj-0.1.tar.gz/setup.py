# Ctrl + / 行注释   Ctrl + Shift + / 块注释
from setuptools import setup,find_packages
setup(
    name="xxxjjj",
    version="0.1",
    author="lxj",
    description="lxj(雷雄杰)_yjr(叶嘉荣)_gz(高湛)",
    packages = find_packages("lxj"),
    package_dir = {"":"lxj"},
    package_data = {
        "":[".txt",".info","*.properties",".py"],
        "":["data/*.*"],
    },
    exclude = ["*.test","*.test.*","test.*","test"]
)
