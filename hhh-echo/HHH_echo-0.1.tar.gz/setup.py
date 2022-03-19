from setuptools import setup,find_packages
setup(
    name="HHH_echo",
    version="0.1",
    author="HHH",
    description="袁力祈,何慧华",
    packages = find_packages("src"),
    package_dir = {"":"src"},
    package_data = {
        "":[".txt",".info","*.properties",".py"],
        "":["data/*.*"],
    },
    exclude = ["*.test","*.test.*","test.*","test"]
)