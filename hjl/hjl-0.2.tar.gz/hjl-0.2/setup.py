from setuptools import setup,find_packages
setup(
    name = "hjl",
    version = "0.2",
    description = "侯金丽_黄咏茵_郭洁迎",
    author = "hjl_hyy_gjy",
    packages = find_packages("hjl"),
    package_dir = {"":"hjl"},
    package_data = {
        "":[".txt",".info","*.properties",".py"],
        "":["data/*.*"],
    },
    exclude = ["*.test","*.test.*","test.*","test"]
)