

from setuptools import setup,find_packages
setup(
name="wcj-handsome",
    version="0.1",
    author="吴昌杰，黄启威",
    packages = find_packages("wcj"),
    package_dir = {"":"wcj"},
    package_data = {
        "":[".txt",".info","*.properties",".py"],
        "":["data/*.*"],
    },
    exclude = ["*.test","*.test.*","test.*","test"]
)
