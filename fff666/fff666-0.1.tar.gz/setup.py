from setuptools import setup,find_packages
setup(
    name="fff666",
    description="冯伟文",
    version="0.1",
    author="fww",
    packages=find_packages("hello"),
    package_dir={"":"hello"},
    package_data={
        "":[".txt",".info","*.properties",".py"],
        "":["data/*.*"],
    },
    exclude=["*.test","*.test.*","test.*","test"]
)