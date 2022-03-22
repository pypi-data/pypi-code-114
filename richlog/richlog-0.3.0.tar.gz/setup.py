from setuptools import setup,find_packages
setup(
    name = "richlog",
    version = "0.3.0",
    keywords = ["pip", "log"],
    description = "log filename timestamp linenumber",
    long_description = "log filename timestamp linenumber",
    license = "MIT Licence",
    url = "https://github.com/metacryptosec/log.git",
    author = "www.metacryptosec.com",
    author_email = "blockchaindeveloper123@gmail.com",
    packages = find_packages(where='src',
                             include=['*']
                             ),
    package_dir={"": "src"},
    include_package_data = True,

    platforms = "any",
    install_requires = []
)