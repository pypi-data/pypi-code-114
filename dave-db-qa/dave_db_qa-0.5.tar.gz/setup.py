from distutils.core import setup
setup(
    name = 'dave_db_qa',
    packages = ['dave_db_qa'],
    version = '0.5',
    license = 'agpl-3.0',
    description = '',
    author = 'David Levy',
    author_email = 'david.g.levy@gmail.com',
    url = 'https://github.com/davidglevy/databricks-qa',
    download_url= 'https://github.com/davidglevy/databricks-qa/archive/v_0.01.tar.gz',
    keywords= ['UTILITY', 'DATABRICKS'],
    install_requires = [
        'pandas'
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8'
    ]
)