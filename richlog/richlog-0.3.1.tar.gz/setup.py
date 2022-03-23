from setuptools import setup,find_packages

setup(
    name = "richlog",
    version = "0.3.1",
    keywords = ["pip", "log"],
    description = "log filename timestamp linenumber",
    long_description = "log filename timestamp linenumber",
    license = "MIT Licence",
    url = "https://github.com/metacryptosec/log.git",
    author = "www.metacryptosec.com",
    author_email = "blockchaindeveloper123@gmail.com",
    package_dir={"":"src"},
    packages = find_packages('src/'),
    include_package_data = True,
    platforms = "any",
    install_requires = [],
    zip_safe=False
)
