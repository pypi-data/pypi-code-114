from setuptools import *

kwargs = {
    "author" : "Nathalon",
    "description" : "mdbttack",
    "entry_points" : {"console_scripts" : ["mdbttack=mdbttack.mdbttack:main"]},
    "license" : "GPL v3",
    "name" : "mdbttack",
    "packages" : ["mdbttack"],
    "version" : "V0.0.1",
    "url" : "https://github.com/Nathalon/mdbttack.git"
}

setup(**kwargs)
