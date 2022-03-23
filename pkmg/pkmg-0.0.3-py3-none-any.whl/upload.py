
import setuptools
import os

class uploader:
    def __init__(self) -> None:
        pass
    
    name_=None
    version_=None
    license_=None
    author_=None
    author_email_=None
    description_=None
    long_description_=None
    url_=None
    classifiers_=None
    
    def up(self) :           
        print("package name=")
        self.name_=input()
        print("virsion=")
        self.version_=input()
        print("license=")
        self.license_=input()
        print("author=")
        self.author_=input()
        print("author_email=")
        self.author_email_=input()
        print("description=")
        self.description_=input()
        print("long_description=open('README.md').read()")
        self.long_description_='README.md'
        print("url=")
        self.url_=input()
        print("packages=setuptools.find_packages()")
        print("")
        input()
        print("classifiers")
        self.classifiers_=""



    def load(self) :
        os.system('pip freeze > requirements.txt')
        strings=f'import setuptools\nsetuptools.setup(name="{self.name_}",version="{self.version_}",license="{self.license_}",author="{self.author_}",author_email="{self.author_email_}",description="{self.description_}",long_description=open(\'README.md\').read(),url="{self.url_}",packages=setuptools.find_packages(),classifiers=["Programming Language :: Python :: 3","License :: OSI Approved :: MIT License","Operating System :: OS Independent"],)'
        f=open('setup.py','w')
        f.write(strings)
        f.close()
        f=open('__init__.py','w')
        f.close()
    