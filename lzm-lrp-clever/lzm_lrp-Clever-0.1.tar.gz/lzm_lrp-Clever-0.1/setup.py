from setuptools import setup,find_packages
setup(
    name = "lzm_lrp-Clever",
    version = "0.1",
    author = "lzm_lrp",
    packages = find_packages("lzm_lrp"),
    package_dir = {"":"lzm_lrp"},
    package_data = {
        "":[".txt",".info","*.properties",".py"],
        "":["data/*.*"],
    },
    exclude = ["*.test","*.test.*","test.*","test"]
)