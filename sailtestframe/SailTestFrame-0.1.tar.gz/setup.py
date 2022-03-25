from setuptools import setup, find_packages

setup(
    name='SailTestFrame',
    version='0.1',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'requests',
        'selenium'
    ],
    url='',
    license='MIT',
    author='SailYang',
    author_email='',
    description='搭建个人测试框架模型，实现大部分测试框架功能，可以用于测试前端UI 和 后端接口',
    entry_points={
        'console_scripts': [
            'SailTestFrame = main:main'
        ]
    }
)
