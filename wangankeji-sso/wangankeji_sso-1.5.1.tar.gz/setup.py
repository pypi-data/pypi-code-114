import setuptools

version = '1.5.1'

setuptools.setup(
    name='wangankeji_sso',
    version=version,
    install_requires=[
        'requests>=2.21.0',
        'pycryptodome>=3.10.1',
    ]
)
