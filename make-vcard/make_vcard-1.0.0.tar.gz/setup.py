import setuptools
import make_vcard

with open("README.md", "r", encoding="utf-8") as f:
    README = f.read()


setuptools.setup(
    name=make_vcard.__name__,
    version=make_vcard.__version__,
    author=make_vcard.__author__,
    author_email="948258209@qq.com",
    description="用于以excel文件生成.vcf通讯录导入文件",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://gitee.com/antianshi/make_vcard", 
    packages=setuptools.find_packages(), 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[ 
        'openpyxl >= 3.0.9',
        'xlrd >= 2.0.1',
        'pandas >= 1.4.1',
    ],
)