import os
from distutils.command.register import register as register_orig
from distutils.command.upload import upload as upload_orig
from setuptools import setup


class register(register_orig):

    def _get_rc_file(self):
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), '.pypirc')


class upload(upload_orig):

    def _get_rc_file(self):
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), '.pypirc')


setup(
    name='sk_wzc',
    packages=['sk_wzc'],
    install_requires=[
        'requests',
    ],
    author="wangzhichen",
    author_email='wzc18811741603@126.com',
    url='https://github.com/username/reponame',
    version='1.1.1',
    # cmdclass={
    #     'register': register,
    #     'upload': upload,
    # }
)
