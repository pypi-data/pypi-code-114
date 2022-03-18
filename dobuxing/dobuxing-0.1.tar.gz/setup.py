from setuptools import setup,find_packages
setup(
name="dobuxing",
version="0.1",
author="xxb",
packages = find_packages("src"),
package_dir = {"":"src"},
package_data = {
"":[".txt",".info","*.properties",".py"],
"":["data/*.*"],
},
exclude = ["*.test","*.test.*","test.*","test"]
)
description="方家伟,黄之迷,谢心冰"
