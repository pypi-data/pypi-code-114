from setuptools import setup,find_packages

setup(
    name = "daiutils",
    version = "0.3.2",
    keywords = ["pip", "log"],
    description = "utilities for coding",
    long_description = "utilities for coding  log",
    license = "MIT Licence",
    url = "https://github.com/golangrustnode/daiutils",
    author = "www.metacryptosec.com",
    author_email = "hacklinux.org@gmail.com",
    package_dir={"":"src"},
    packages = find_packages('src/'),
    include_package_data = True,
    platforms = "any",
    install_requires = [],
    zip_safe=False
)
