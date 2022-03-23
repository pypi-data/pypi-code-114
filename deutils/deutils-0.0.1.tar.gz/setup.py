from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 3 - Alpha', 
    'Intended Audience :: Developers',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='deutils',
    version = '0.0.1',
    description = 'includes Google Cloud, AWS, Snowflake, PySpark and some data manipulation functions',
    long_description = open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Weiang Li',
    author_email='weiangli1995@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords = '',
    packages=find_packages(),
    install_requires=['boto3==1.20.23','sqlalchemy==1.4.28','snowflake-connector-python==2.7.1','google-api-python-client==2.33.0','pyspark==3.2.1','pandavro==1.6.0']
)