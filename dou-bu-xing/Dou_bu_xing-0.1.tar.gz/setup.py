from setuptools import setup,find_packages
setup(
    name="Dou_bu_xing",
    version="0.1",
    author="Wai",
    description = '两爹（谢心冰、黄之迷、武警冰）带一儿（方家伟）',
    packages = find_packages("fjw"),
    package_dir = {"":"fjw"},
    package_data = {
        "":[".txt",".info","*.properties",".py"],
        "":["data/*.*"],
    },
    exclude = ["*.test","*.test.*","test.*","test"]
)