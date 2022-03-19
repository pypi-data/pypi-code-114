import setuptools

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

with open("requirements.txt", encoding="utf-8") as file:
    install_requires = file.read()

setuptools.setup(
    name="sai-logger",
    version="0.0.2",
    author="saito-ya",
    author_email="yasuosaito13@gmail.com",
    description="packege for pypi test",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    python_requires=">=3.7",
    include_package_data=True,
)