from distutils.core import setup

setup(
    name = 'haohan_unittest',#需要打包的名字
    version = 'v1.0',#版本
    author = 'Javen', # 作者
    packages = ['', 'test', 'test/testmock']#需要打包的模块
)