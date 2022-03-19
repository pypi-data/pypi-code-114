from setuptools import setup,find_packages
setup(
    name="GD_1C302",
    version="0.1",
    author="GD",
    description = "The members of our team are 肖俊毅,梁景洛 and 谭剑辉",
    packages = find_packages("GD"),
    package_dir = {"":"GD"},
    package_data = {
        "":[".txt",".info","*.properties",".py"],
        "":["data/*.*"],
    },
    exclude = ["*.test","*.test.*","test.*","test"]
)