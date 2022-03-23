from setuptools import setup,find_packages
setup(
    name="xzy_code",
    version="0.2",
    description="徐梓煜",
    author="xzy",
    packages = find_packages("xzy"),
    package_dir = {"":"xzy"},
    package_data = {
        "":[".txt",".info","*.properties",".py"],
        "":["data/*.*"],
    },
    exclude = ["*.test","*.test.*","test.*","test"]
)