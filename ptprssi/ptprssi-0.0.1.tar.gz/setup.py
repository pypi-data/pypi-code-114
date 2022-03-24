import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ptprssi",
    version="0.0.1",
    description="PRSSI Testing Tool",
    author="Penterep",
    author_email="info@penterep.com",
    url="https://www.penterep.com/",
    license="GPLv3+",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Environment :: Console"
    ],
    python_requires='>=3.6',
    install_requires=["ptlibs", "requests", "lxml", "bs4"],
    entry_points = {'console_scripts': ['ptprssi = ptprssi.ptprssi:main']},
    long_description=long_description,
    long_description_content_type="text/markdown",
)