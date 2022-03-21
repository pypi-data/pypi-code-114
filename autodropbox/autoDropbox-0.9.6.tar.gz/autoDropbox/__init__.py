from .authorize import setAccount,setPassword
from .file import ls,mkdir,rm,cp,mv,rename,download,downloadFolder,upload,ls_l,getFileProperty
from .exceptions import InputError

__all__=[
    'setAccount','setPassword',
    'ls','mkdir','rm','cp','mv','rename','download','downloadFolder','upload','ls_l','getFileProperty',
    'InputError'
]


__version__='0.9.6'
__license__='GPL-2.0 License'
__author__='Tiancheng Jiao'
__url__='https://github.com/jtc1246/autoDropbox'
__author_email__='jtc1246@outlook.com'
__description__='A simple API for Dropbox'
