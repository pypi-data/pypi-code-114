from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="EvalSafe",
    version="1",
    author="Zedikon",
    author_email="mrzedikon@gmail.com",
    description="Calculate expressions in a string using eval without security threats!",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Zedikon/EvalSafe",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)