from setuptools import setup,find_packages
setup(
    name="ywl-handsome",
    version="0.1",
    author="ywl",
    description="组长：方俊龙，组员：叶文龙",
    packages = find_packages("ywl"),
    package_dir = {"":"ywl"},
    package_data = {
        "":[".txt",".info","*.properties",".py"],
        "":["data/*.*"],
    },

    exclude = ["*.test","*.test.*","test.*","test"]
)