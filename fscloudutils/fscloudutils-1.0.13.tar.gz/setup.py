import setuptools

setuptools.setup(
    name='fscloudutils',
    packages=['fscloudutils'],
    version='1.0.13',
    license='MIT',
    python_requires='>=3.6',
    description="A package for all fs cloud utilities",
    author="Yotam Raz",
    install_requires=["scikit-image", "pillow", "requests", "boto3", "mysql", "mysql-connector-python-rf", "pandas"]
)
