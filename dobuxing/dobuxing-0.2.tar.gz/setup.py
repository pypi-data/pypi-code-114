from setuptools import setup,find_packages
setup(
name="dobuxing",
version="0.2",
author="xxb",
packages = find_packages("src"),
package_dir = {"":"src"},
description="方家伟,黄之迷,谢心冰",
package_data = {
    "":[".txt",".info","*.properties",".py"],
    "":["data/*.*"],
},
exclude = ["*.test","*.test.*","test.*","test"]
)
