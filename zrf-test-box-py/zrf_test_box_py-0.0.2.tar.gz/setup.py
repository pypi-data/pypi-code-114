from setuptools import setup, find_packages
 
setup(
    #pip install nnn
    name = "zrf_test_box_py", 
    version = "0.0.2",
    # keywords = ("pip", "pandas", "pd"),
    description = "短描述",
    long_description = "长描述",
    #协议
    # license = "GPL Licence",
 
    url = "https://github.com/xxx",
    author = "xxx",
    author_email = "xxx@xxx.com",
 
    #自动查询所有"__init__.py"
    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    #提示前置包
    install_requires = ['requests']
)