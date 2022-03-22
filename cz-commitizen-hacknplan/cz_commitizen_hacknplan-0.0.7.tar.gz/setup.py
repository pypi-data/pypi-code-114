import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cz_commitizen_hacknplan",
    version="0.0.7",
    author='Nigel George',
    author_email='nigel.george@shiroikuma.co.uk',
    url='https://github.com/CanisHelix/commitizen_hacknplan',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="MIT",
    long_description="A variation of conventional commits with HackNPlan Tasks.",
    install_requires=["commitizen"],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)