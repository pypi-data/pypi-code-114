import re
import shutil
import sys

import setuptools
from setuptools import setup
import os

"""


"""

app_name = "mytodo2"

this_directory = os.path.abspath(os.path.dirname(__file__))

# 读取文件内容
def read_file(filename):
    with open(os.path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description


# 指定要安装的package
def get_packages(package):
    """Return root package and all sub-packages."""
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


# 获取依赖
def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]


my_packages = []
# my_packages.extend(get_packages("package1"))
# my_packages.extend(get_packages("package2"))
my_packages.extend(get_packages("src"))
print("my_packages:", my_packages)

my_requirements = read_requirements('requirements.txt')
print("my_requirements:", my_requirements)


def publish():
    """上传"""
    # 检查打包工具
    if os.system("pip freeze | findstr twine"):
        print("twine not installed.\nUse `pip install twine`.\nExiting.")
        sys.exit()
    # 上传
    os.system("python -m twine upload --repository pypi dist/*")


def make():
    """打包"""
    if os.path.exists("./dist"):
        shutil.rmtree("dist")
    # 打包
    os.system("python setup.py sdist bdist_wheel")


def get_version():
    """Return package version as listed in `__version__` in `init.py`."""
    init_py = open(os.path.join("src", app_name, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def install():
    """安装包到本地环境"""
    version = get_version()
    os.system(f" python -m pip install ./dist/{app_name}-{version}.tar.gz")


if sys.argv[-1] == 'publish':
    make()
    publish()
    sys.exit()
elif sys.argv[-1] == 'make':
    make()
    # install()
    sys.exit()

setup(
    name=app_name,
    version=get_version(),
    author='yangzhi',
    author_email='y.zhisky@163.com',
    url='http://www.zhim.top',
    license='MIT Licence',
    description='Project documentation with Markdown.',
    long_description=read_file('README.md'),  # 读取的Readme文档内容
    long_description_content_type="text/markdown",  # 指定包文档格式为markdown
    platforms="any",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    # 包含非python脚本文件,搭配MANIFEST.in使用
    include_package_data=True,
    # 需要安装的依赖
    install_requires=my_requirements,
    python_requires='>=3.5',
    # 添加这个选项，在windows下Python目录的scripts下生成exe文件, 注意：模块与函数之间是冒号:
    entry_points={
        'console_scripts': [
            # 'test1 = package1.test2:cli',
            # 'test4 = package2.test4:main1',
            'mytodo = mytodo.todo:main',
        ]
    },
    # 程序的所属分类列表
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        'Topic :: Documentation',
        'Topic :: Text Processing',
    ],
    # 此项需要，否则卸载时报windows error
    zip_safe=False,
)
