from setuptools import setup, find_packages
setup(
    name="cbh-666",
    version="0.1",
    author="cbh",
    packages=find_packages("cbh"),
    package_dir={"":"cbh"},
    package_data={
        "":[".txt",".info","*.properties",".py"],
        "":["data/*.*"],
    },
    exclude=["*.test","*.test.*","test.*","test"]
)
