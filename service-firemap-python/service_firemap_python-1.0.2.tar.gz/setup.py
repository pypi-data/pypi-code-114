"""
FireMap data microservice in Python
----------------------

"""

from setuptools import find_packages
from setuptools import setup

try:
    readme = open('readme.md').read()
except:
    readme = __doc__

setup(
    name='service_firemap_python',
    version='1.0.2',
    url='https://gitlab.com/eic-stopfires/service-firemap-python',
    # license='MIT',
    author='Conceptual Vision Consulting LLC',
    # author_email='seroukhov@gmail.com',
    description='FireMap data microservice in Python',
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=['config', 'data', 'test']),
    include_package_data=True,
    zip_safe=True,
    platforms='any',
    install_requires=[
        'pip-services3-commons >= 3.3.11, < 4.0',
        'pip-services3-components >= 3.5.4, < 4.0',
        'pip-services3-container >= 3.2.3, < 4.0',
        'pip-services3-data >= 3.2.3, < 4.0',
        'pip-services3-rpc >= 3.3.1, < 4.0',
        'pip-services3-swagger >= 3.0.2, < 4.0',
        'pip-services3-mongodb >= 3.2.3, < 4.0',
        'pip-services3-messaging >= 3.1.1, < 4.0',
        'pip-services3-kafka >= 3.1.7, < 4.0'
    ],
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)
