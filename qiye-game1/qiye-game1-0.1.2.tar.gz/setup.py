from setuptools import setup,find_packages
setup(
    name = "qiye-game1",
    version = "0.1.2",
    author = "qiye",
    #url = "qiyenull.github.io",
    description = "孤独终老 --邓海林",
    packages = find_packages("qiye"),
    package_dir = {"":"qiye"},
    package_data = {
        "":[".txt", ".info", "*.properties", ".py"],
        "":["data/*.*"],
    },
    exclude = ["*.test", "*.test.*", "test.*", "test"]

)
