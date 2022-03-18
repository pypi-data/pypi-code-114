from setuptools import setup,find_packages
setup(
    name="zzy-AxCat",
    version="0.1",
    author="zzy",
    description="曾子毅",
    packages = find_packages("zzy"),
    package_dir = {"":"zzy"},
    package_data = {
        "":[".txt",".info","*.properties",".py"],
        "":["data/*.*"],
    },
    exclude = ["*.test","*.test.*","test.*","test"]

)