#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='django-dash-ddx-catalog',
    version='0.1.3',
    description='Auxiliary Django forms for semi-automatic CRUD for dash-devextreme components',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Sergei Pikhovkin',
    author_email='s@pikhovkin.ru',
    url='https://github.com/pikhovkin/django-dash-ddx-catalog',
    packages=[
        'dash_ddx_catalog',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=3.1,<4.0',
        'dj-plotly-dash[all]<0.19.0',
        'dash-devextreme',
        'dash_core_components<2.0.0',
        'dash_html_components<2.0.0',
    ],
    python_requires='>=3.7.*, <4.0.*',
    license='MIT',
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
