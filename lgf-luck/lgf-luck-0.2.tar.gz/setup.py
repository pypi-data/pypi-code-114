from setuptools import setup,find_packages
setup(
    name="lgf-luck",
    version="0.2",
    author="lgf",
    description="lgf",
    packages=find_packages("lgf"),
    package_dir={"":"lgf"},
    package_data={
        "":[".txt",".info","*.properties",".py"],
        "":["data/*.*"],
    },
    exclude=["*.test","*.test.*","test.*","test"]
)