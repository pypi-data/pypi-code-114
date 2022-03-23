import os
import re
import shutil
import sys

import setuptools

this_directory = os.path.abspath(os.path.dirname(__file__))

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


# 读取文件内容
def read_file(filename):
    with open(os.path.join(this_directory, filename), encoding='utf-8') as f:
        data = f.read()
    return data


# 获取依赖
def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]


def get_version():
    """Return package version as listed in `__version__` in `init.py`."""
    init_py = open(os.path.join("src", "mypk1", '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def publish():
    """上传"""
    # 检查打包工具
    if os.system("pip freeze | findstr twine"):
        print("twine not installed.\nUse `pip install twine`.\nExiting.")
        sys.exit()
    # 上传
    os.system("python -m twine upload --repository pypi dist/*")
    print("You probably want to also tag the version now:")


def make():
    """打包"""
    if os.path.exists("./dist"):
        shutil.rmtree("dist")
    # 打包
    os.system("python setup.py sdist bdist_wheel")


def install():
    """安装包到本地环境"""
    version = get_version()
    os.system(f" python -m pip install ./dist/mypk1-{version}.tar.gz")


if sys.argv[-1] == 'publish':
    make()
    publish()
    sys.exit()
elif sys.argv[-1] == 'make':
    make()
    install()
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
    # install_requires=read_requirements('requirements.txt'),
    entry_points={
        'console_scripts': [
            # 'test1 = package1.test2:cli',
            # 'test4 = package2.test4:main1',
            'test1 = mypk1.example:cli',
        ]
    },
    # 包含非python脚本文件,搭配MANIFEST.in使用
    include_package_data=True,
    zip_safe=False,
)
