from setuptools import setup,find_packages
setup(
    name="cxj-handsome",
    version="0.1",
    author="cxj",
    packages = find_packages("cxj"),
    package_dir = {"":"cxj"},
    package_data = {
        "":[".txt",".info","*.properties",".py"],
        "":["data/*.*"],
    },
    exclude = ["*.test","*.test.*","test.*","test"]
)