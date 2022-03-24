from setuptools import setup

classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Education',
    'License :: OSI Approved :: Apache Software License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
]

setup(
    name='pnwcybersec',
    packages=['pnwcybersec'],
    package_dir={'pnwcybersec': 'src/pnwcybersec'},
    package_data={'pnwcyersec': ['data/*.txt']},
    version='0.2.5',
    description='A deep learning malware detection module.',
    long_description='A Deep Learning Malware Detection Module.\nFor GPU support see: https://pytorch.org/get-started/locally/',
    long_description_content_type='text/markdown',
    url = 'https://github.com/bbdcmf/pnwcybersec',
    project_urls={
        "Bug Tracker": "https://github.com/bbdcmf/pnwcybersec/issues",
    },
    author = 'Ryan Frederick, Joseph Shapiro',
    author_email='freder20@pnw.edu',
    license='Apache License 2.0',
    classifiers=classifiers,
    keywords='Deep Learning, Cyber Security',
    install_requires=['fastai', 'numpy', 'pillow', 'matplotlib']
)
