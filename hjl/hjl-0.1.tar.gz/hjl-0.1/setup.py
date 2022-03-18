from setuptools import setup,find_packages
setup(
    name = "hjl",
    version = "0.1",
    author = "hjl_hyy_gjy",
    packages = find_packages("hjl"),
    package_dir = {"":"hjl"},
    package_data = {
        "":[".txt",".info","*.properties",".py"],
        "":["data/*.*"],
    },
    exclude = ["*.test","*.test.*","test.*","test"]
)