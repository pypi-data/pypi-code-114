import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
        name='usernado',
        version='0.0.5',
        author='Morteza Naghizadeh',
        author_email='rreganto@gmail.com',
        description='Tornado Boilerplate for Human',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://github.com/reganto/Usernado',
        packages=setuptools.find_packages(),
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: OS Independent',
        ],
        python_requires='>=3.6',
        install_requires=[
            'tornado',
        ],
        keywords='tornado boilerplate',
        project_urls={
            'Homepage': 'https://github.com/reganto/Usernado',
        },
        entry_points={
            'console_scripts': [
                'usernado=handlers.usernado.__main__:main',
            ],
        },
)
