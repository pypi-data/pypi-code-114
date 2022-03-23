from setuptools import setup, find_packages
 
__version__ = '1.0' # 版本号
 
setup(
    name = 'tss_coco', # 在pip中显示的项目名称
    version = __version__,
    author = 'Dechin',
    author_email = 'dechin.phy@gmail.com',
    long_description_content_type="text/markdown",
    url = ' ',
    description = 'ts: Test Setup',
    python_requires = '>=3.5.0',
    packages=['ts']
    )   