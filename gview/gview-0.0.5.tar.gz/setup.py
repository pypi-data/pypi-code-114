import setuptools

setuptools.setup(
    name ='gview',
    version = '0.0.5',
    description = 'a RESTful web application to monitor GPU usage across multiple servers',
    author = 'Brandon S',
    author_email = 'brankond@gmail.com',
    packages=['gview'],
    package_dir={'':'src'},
    package_data={'gview':['static/css/*','static/js/*','templates/*','Hosts.txt','run.sh']},
    entry_points={
        'console_scripts': [
            'gview=gview.run:run',
        ],
    }
)