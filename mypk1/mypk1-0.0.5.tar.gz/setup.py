import os
import re
import shutil
import sys

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


def get_version():
    """Return package version as listed in `__version__` in `init.py`."""
    init_py = open(os.path.join("src", "mypk1", '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def publish():
    # 检查打包工具
    if os.system("pip freeze | findstr twine"):
        print("twine not installed.\nUse `pip install twine`.\nExiting.")
        sys.exit()
    # 上传
    # os.system("twine upload dist/*")
    os.system("python -m twine upload --repository pypi dist/*")
    print("You probably want to also tag the version now:")
    # version = get_version()
    # 创建git tag并上传
    # print(f"  git tag -a {version} -m 'version {version}'")
    # print("  git push --tags")


def make():
    if os.path.exists("./dist"):
        # os.rmdir("dist")
        shutil.rmtree("dist")
    # 打包
    os.system("python setup.py sdist bdist_wheel")


if sys.argv[-1] == 'publish':
    make()
    publish()
    sys.exit()
elif sys.argv[-1] == 'make':
    make()
    sys.exit()


setuptools.setup(
    name="mypk1",
    version=get_version(),
    author="yangzhi",
    author_email="y.zhisky@163.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
