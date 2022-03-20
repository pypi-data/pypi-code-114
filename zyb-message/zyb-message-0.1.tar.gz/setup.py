from setuptools import setup,find_packages
setup(
    name="zyb-message",
    version="0.1",
    author="zyb",
   description = "张奕标，陈兴金",
    packages = find_packages("zyb"),
    package_dir = {"":"zyb"},
    package_data = {
        "":[".txt",".info","*.properties",".py"],
        "":["data/*.*"],
    },
    exclude = ["*.test","*.test.*","test.*","test"]
)

