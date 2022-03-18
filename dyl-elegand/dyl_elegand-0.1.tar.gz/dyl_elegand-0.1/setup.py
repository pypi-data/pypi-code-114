from setuptools import setup,find_packages
setup(
    name = "dyl_elegand",
    version = "0.1",
    author = "dyl.dsh.cfr",
    packages = find_packages("dyl"),
    package_dir = {"":"dyl"},
    package_data = {
        "":[".txt",".info","*.properties",".py"],
        "":["data/*.*"],
    },
    exclude = ["*.test","*.test.*","test.*","test"]
)