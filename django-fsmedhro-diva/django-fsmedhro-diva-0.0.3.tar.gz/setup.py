import os
from setuptools import find_packages, setup

with open('README.md', 'r', encoding='utf-8') as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-fsmedhro-diva',
    version='0.0.3',
    author='Martin Darmüntzel',
    author_email='martin@trivialanalog.de',
    description='Django-App für die Auswertung von Veranstaltungen',
    packages=find_packages(),
    include_package_data=True,
    long_description=README,
    long_description_content_type="text/markdown",
    license='MIT License',
    url='https://github.com/hutchison/django-exoral',
    install_requires=[
        'Django>=3.0',
        'django-fsmedhro-core>=0.2.6',
    ],
    python_requires=">=3.5",
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
