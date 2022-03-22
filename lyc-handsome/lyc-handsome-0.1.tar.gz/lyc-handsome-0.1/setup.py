from setuptools import setup,find_packages
setup(
name="lyc-handsome",
    version="0.1",
    author="lyc",
    description="组长：李亚成，组员：谢秉求，郭高举",
    packages = find_packages("lyc"),
    package_dir = {"":"lyc"},
    package_data = {
    "":[".txt",".info","*.properties",".py"],
    "":["data/*.*"],
    },

    exclude = ["*.test","*.test.*","test.*","test"]
)
