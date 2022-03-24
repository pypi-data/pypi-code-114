#!/usr/bin/env python3
import os
import sys

# Python 3.8 or later needed
if sys.version_info[:2] < (3, 8):
    raise RuntimeError("Python version >= 3.8 required.")

CLASSIFIERS = """\
Development Status :: 1 - Planning
Environment :: Console
Intended Audience :: Education
Intended Audience :: Science/Research
License :: OSI Approved :: MIT License
Natural Language :: English
Operating System :: POSIX :: Linux
Operating System :: MacOS
Programming Language :: Python :: 3.8
Topic :: Scientific/Engineering
"""
      
def setup_package():
    src_path = os.path.dirname(os.path.abspath(__file__))
    old_path = os.getcwd()
    os.chdir(src_path)
    sys.path.insert(0, src_path)
    
    # Project name
    name = "optimate"
    
    # Project description read from file
    long_description = open(os.path.join(src_path, 'README.md')).read()
    
    # Build a list of all project modules
    packages = []
    for dirname, dirnames, filenames in os.walk(name):
        if '__init__.py' in filenames:
            packages.append(dirname.replace('/', '.'))
            
    package_dir = {name: name}

    ## Data files used e.g. in tests
    #package_data = {name: [os.path.join(name, 'tests', 'prt.txt')]}
    
    # The current version number - MSI accepts only version X.X.X
    #version = open(os.path.join(src_path, name, 'version.py')).read()
    
    # Scripts
    scripts = []
    for dirname, dirnames, filenames in os.walk('bin'):
        for filename in filenames:
            if not filename.endswith('.bat'):
                scripts.append(os.path.join(dirname, filename))
                
    ## Provide bat executables in the tarball (always for Win)
    #if 'sdist' in sys.argv or os.name in ['ce', 'nt']:
        #for s in scripts[:]:
            #scripts.append(s + '.bat')
            
    # Data_files (e.g. doc) needs (directory, files-in-this-directory) tuples
    data_files = []
    for dirname, dirnames, filenames in os.walk('doc'):
        fileslist = []
        for filename in filenames:
            fullname = os.path.join(dirname, filename)
            fileslist.append(fullname)
        data_files.append(('share/' + name + '/' + dirname, fileslist))
        
    with open(os.path.join(src_path, 'requirements.txt')) as f:
        requirements = f.read().splitlines()
    
    metadata = dict(
        name=name,
        version='0.0.1',
        description='optimate - parameter optimizer for different material models',
        long_description=long_description,
        long_description_content_type="text/markdown",
        url='',
        author='Muhammad Mohsin Khan',
        author_email='mohsin.khan1@outlook.com',
        license='MIT',
        classifiers=[_f for _f in CLASSIFIERS.split('\n') if _f],
        platforms=["Linux", "Mac OS-X", "Unix"],
        data_files=data_files,
        keywords='optimizer minimizer parameters',
        packages=packages,
        package_dir=package_dir,
        #package_data=package_data,
        scripts=scripts,
        python_requires=">=3.8",
        install_requires=requirements,
      )
    
    try:
        from setuptools import setup
        setup(**metadata)
        
    finally:
        del sys.path[0]
        os.chdir(old_path)
        
    return

if __name__ == '__main__':
    setup_package()
