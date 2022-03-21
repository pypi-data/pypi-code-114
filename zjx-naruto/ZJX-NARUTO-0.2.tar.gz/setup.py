from setuptools import setup,find_packages
setup(
    name="ZJX-NARUTO",
    version="0.2",
    author="zjx",
    description="zjx",
    packages = find_packages("ZJX"),
    package_dir = {"":"ZJX"},
    package_data = {
        "":[".txt",".info","*.properties",".py"],
        "":["data/*.*"],
    },
    exclude = ["*.test","*.test.*","test.*","test"]
)