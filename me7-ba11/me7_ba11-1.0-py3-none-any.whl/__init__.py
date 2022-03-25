"""Python meatball. it's manage your data"""
#
# Package of meatball...it mean manage datas
#
# meatball/__init__.py
#
# Copyright Line CTF 2022, 
#

from pkgutil import extend_path


import sys


__author__ = 'wulfsek'
__author_email__ = 'park.jiho@linecorp.com'
__maintainer__ = 'wulfsek'
__contact__ = "park.jiho@linecorp.com"
__homepage__ = "https://line.me/"
__docformat__ = "restructuredtext"
__path__ = extend_path(__path__, __name__)
# -eof meta-

#
# Copy stuff from default context
#

__all__ = ['config', 'encrypt', 'manage', 'struct']


#
# init main module
#

if '__main__' in sys.modules:
    sys.modules['__mp_main__'] = sys.modules['__main__']

#
# meatball Initialized
#

