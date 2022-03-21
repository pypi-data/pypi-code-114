from setuptools import setup,find_packages
setup(
    name = "zzw.py",
    version = "0.1",
    author = "zzw",
    description="曾卓文，林镇坤",
    packages = find_packages("zzw"),
    package_dir = {"":"zzw"},
    package_data = {
        "":[".txt",".nfo","*.properties",".py"],
        "":["data/*.*"],
    },
    exclude = ["*.test",".test.*","test.*","test"]
)