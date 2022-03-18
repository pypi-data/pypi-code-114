from setuptools import setup,find_packages
setup(
    name = "qiye-game1",
    version = "0.1.1",
    author = "qiye",
    #url = "qiyenull.github.io",
    description = "孤独终老",
    packages = find_packages("qiye"),
    package_dir = {"":"qiye"},
    package_data = {
        "":[".txt", ".info", "*.properties", ".py"],
        "":["data/*.*"],
    },
    exclude = ["*.test", "*.test.*", "test.*", "test"]

)
