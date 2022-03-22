from setuptools import setup,find_packages
setup(
    name="lyp-handsome",
    version="0.1",
    author="lyp",
    packages = find_packages("lyp"),
    package_dir = {"":"lyp"},
    package_data = {
        "":[".txt",".info","*.properties",".py"],
        "":["data/*.*"],
    },
    exclude = ["*.test","*.test.*","test.*","test"]
)