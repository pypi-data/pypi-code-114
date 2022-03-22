from setuptools import setup

setup(
    name='pytest_multithreading_allure',
    version="1.0.5",
    license='MIT',
    description='pytest_multithreading_allure',

    long_description_content_type='text/markdown',
    author='zhujiahuan',
    author_email='zhujiahuan@yfcloud.com',
    include_package_data=True,
    install_requires=['pytest>=3.6','allure-pytest'],
    packages=['pytest_multithreading_allure'],
    entry_points={
        'pytest11': [
            'pytest_multithreading_allure = pytest_multithreading_allure'
        ]
    }
)
