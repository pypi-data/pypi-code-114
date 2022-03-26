from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='post-from-os',
    license='MIT',
    author='epicmanmoo',
    description='Opensea Sales Bots',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author_email='mooaz09@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/epicmanmoo/post-from-os',
    keywords='Bots',
    install_requires=[
        'fake_useragent',
        'requests',
        'tinydb',
        'twython'
      ],
    python_requires='>=3.6'
)
