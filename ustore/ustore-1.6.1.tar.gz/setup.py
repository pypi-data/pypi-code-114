from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='ustore',
    version='1.6.1',    
    long_description=long_description,
    long_description_content_type='text/markdown',
    description='A libary that makes user managment easier.',
    url='https://github.com/JKincorperated/ustore/',
    author='JKinc',
    packages = ['ustore'],
    license='CC BY-NC-SA 4.0',
    author_email='offical.jkinc@gmail.com',
    install_requires=['pyaes',
                      ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3.9',
    ],
)
