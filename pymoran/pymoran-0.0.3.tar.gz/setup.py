# from setuptools import setup, find_packages

# setup(
#     name='pymoran',
#     version='0.0.1',
#     # 包括在安装包内的 Python 包
#     packages=find_packages()
# )
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pymoran",
    version="0.0.3",
    author="Moran",
    author_email="wqmoran@163.com",
    description="简单的自用包",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject",
    # project_urls={
    #     "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    # },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)