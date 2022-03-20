from distutils.core import setup

setup(
    name = 'haohan_unittest',#需要打包的名字
    version = 'v1.1',#版本
    author = 'Javen', # 作者
    packages = ['unittest', 'unittest/test', 'unittest/test/testmock']#需要打包的模块
)