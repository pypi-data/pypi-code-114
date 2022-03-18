from setuptools import setup,find_packages
setup(
    name = "dsh-DSH",
    version = "0.1",
    author = "dyl.dsh.cfr",
    packages = find_packages("dsh"),
    package_dir = {"":"dsh"},
    package_data = {
        "":[".txt",".info","*.properties",".py"],
        "":["data/*.*"],
    },
    exclude = ["*.test","*.test.*","test.*","test"]
)