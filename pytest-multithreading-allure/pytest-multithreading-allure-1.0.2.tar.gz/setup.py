from setuptools import setup

setup(
    name='pytest-multithreading-allure',
    version="1.0.2",
    license='MIT',
    description='pytest-multithreading-allure',

    long_description_content_type='text/markdown',
    author='zhujiahuan',
    author_email='zhujiahuan@yfcloud.com',
    include_package_data=True,
    install_requires=['pytest>=3.6','allure-pytest'],
    packages=['pytest-multithreading-allure'],
    entry_points={
        'pytest11': [
            'th = pytest_th',
        ]
    }
)
