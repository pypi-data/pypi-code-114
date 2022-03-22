from setuptools import setup,find_packages
setup(
    name="LS_GOAT",
    version="0.1",
    author="lld",
    description="组长：林隆达,组员：沈保双",
    packages = find_packages("lld"),
    package_dir = {"":"lld"},
    package_data = {
    "":[".txt",".info","*.properties",".py"],
    "":["data/*.*"],
    },
    exclude = ["*.test","*.test.*","test.*","test"]
)