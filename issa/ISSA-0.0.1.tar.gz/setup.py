from setuptools import setup

setup(
    name='ISSA',
    version='0.0.1',    
    description='A Python Package for the Scritpting of blackbox Tools',
    url='https://github.com/brancokm/ISSA',
    author='Michael Branco-Katcher',
    author_email='brancokm@oregonstate.edu',
    license='MIT',
    packages=['ISSA'],
    install_requires=['scipy>=1.0',
                      'numpy', 
                      'matplotlib',                   
                      ],

    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',  
        'Programming Language :: Python :: 3.8',
    ],
)