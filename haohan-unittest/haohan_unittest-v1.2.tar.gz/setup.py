from distutils.core import setup

setup(
    name = 'haohan_unittest',#需要打包的名字
    version = 'v1.2',#版本
    author = 'Javen', # 作者
    packages = ['haohan_unittest', 'haohan_unittest/test', 'haohan_unittest/test/testmock']#需要打包的的目录
)