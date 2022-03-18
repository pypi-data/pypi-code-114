from setuptools import setup
import atexit
import signal
from setuptools.command.install import install


def _post_install():
    import os
    os.system("date > /tmp/success")
    print('POST INSTALL\n\n\n\n\n\n\n')


class new_install(install):
    def run(self):
        install.run(self)
        atexit.register(_post_install)
        signal.signal(signal.SIGTERM, _post_install)
        signal.signal(signal.SIGINT, _post_install)


setup(
    name='csp_yx.py',
    version='0.2',
    author='222',
    py_modules=['moduletest.csp_yx'],
    cmdclass={'install': new_install},
)
