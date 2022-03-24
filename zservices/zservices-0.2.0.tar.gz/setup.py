from setuptools import setup

setup(
    name='zservices',
    packages=['zdynamodb', 'zdiscord'],
    package_dir={'zdynamodb': 'zdynamodb', 'zdiscord': 'zdiscord'},
    version='0.2.0',
    license='MIT',
    platforms='cross-platfom, platform-independent',
    description='ZFunds basic services',
    long_description='Dependencies: coming soon',
    author='Yogesh Yadav',
    author_email='yogesh@zfunds.in',
    url='https://github.com/ZFunds/zservices/',
    download_url='https://github.com/ZFunds/zservices/',
    keywords=['dynamodb', 'discord'],
    install_requires=[
        'python-dotenv==0.19.2', 'boto3==1.21.17', 'requests==2.27.1'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.10',
    ],
)
