from setuptools import setup

setup(
    name='zservices',
    packages=['zdynamodb'],
    package_dir={'zdynamodb': 'zdynamodb'},
    version='0.1.9',
    license='MIT',
    platforms='cross-platfom, platform-independent',
    description='ZFunds basic services',
    long_description='Dependencies: coming soon',
    author='Yogesh Yadav',
    author_email='yogesh@zfunds.in',
    url='https://github.com/ZFunds/zservices/',
    download_url='https://github.com/ZFunds/zservices/',
    keywords=['dynamodb'],
    install_requires=[
        'python-dotenv==0.19.2', 'boto3==1.21.17'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.10',
    ],
)
