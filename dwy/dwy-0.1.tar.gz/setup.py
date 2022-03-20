from setuptools import setup,find_packages
setup(
name="dwy",
version="0.1",
author="dwy",
packages = find_packages("src"),
package_dir = {"":"src"},
description="邓文怡",
package_data = {
    "":[".txt",".info","*.properties",".py"],
    "":["data/*.*"],
},
exclude = ["*.test","*.test.*","test.*","test"]
)
