# -*- coding: utf-8 -*-
'''

Created on 8/03/2022 from ganessa

@author: Jarrige_Pi

Determines where and which dll to use

'''
from __future__ import (unicode_literals, print_function, absolute_import)
from importlib import import_module
from itertools import product, chain

import os.path as OP
from os import environ

from ganessa.util import unistr, ws
from ganessa._getdll import AddDllDirectory

debuglevel = 0

def _import_pendulo(test=True):
    '''Search for the most recent version of compatible pyganessa dll '''
    pydll = '_pyPendulo'
    try:
        mod = import_module('.' + pydll, package='pendulo')
    except ImportError:
        if debuglevel > 0:
            print('\t', 'error; mode=', 'test' if test else 'activation')
        return False
    else:
        if test:
            del mod
            return True
        # print(f'  --->  using interface <{pydll}>')
        return mod

def _getdllinfo():
    ''' Locates the simulation kernel - Penwin32.dll
        in an expected folder and ensures that an appropriate .pyd
        interface exists (EnvSearchError)

        Folder are looked up in the following order:
        - PENDULO_DIR environment variable
        - folder list from PATH environment variable for either dll
        - default installation folders for Pendulo
        - for FR, eng, esp
    '''
    f = 'PenWin32.dll'
    for pen_dir in ('PENDULO_DIR', ):
        if pen_dir in environ:
            pendir = unistr(environ[pen_dir])
            if OP.exists(OP.join(pendir, f)):
                print(f, 'found in environment variable', pen_dir, end=' ')
                with AddDllDirectory(pendir):
                    if _import_pendulo():
                        print(' :-)')
                        break
                    print(' but *NOT* responding !')
            else:
                print(f, ' ** NOT ** found in environment variable', pen_dir)
    else:
        # if none succeeds examine PATH variable
        for pendir in unistr(environ['path']).split(';'):
            if OP.exists(OP.join(pendir, f)):
                if debuglevel > 0:
                    print(ws(f + ' found in Path: ' + pendir))
                with AddDllDirectory(pendir):
                    if _import_pendulo():
                        break
        # finally check default installation paths
        else:
            if debuglevel:
                print(' * no dll found in PATH environment variable folders')
            # then default installation folders:
            # (drive) (program folder) (editor name) (software_lang) (dll)
            PROG6_x32 = environ.get('ProgramFiles(x86)', '/Program Files (x86)')
            PROG_USR = OP.join(environ['LOCALAPPDATA'], 'Programs')
            # Piccolo floder is Piccolo_lang for Safege and Piccolo6_lang for Gfi/Inetum
            pfld_name = 'Pendulo'
            dpes = tuple((PROG_USR, saf) for saf in ('Safege', 'Suez'))
            pes = ((PROG6_x32, 'Safege'), )
            partition = ('D:', 'C:') if OP.exists('D:/') else ('C:',)
            if OP.exists('E:/') and len(partition) == 1:
                partition = ('E:', 'C:')
            ppes = ((d + OP.splitdrive(p)[1], e)
                        for d, (p, e) in product(partition, pes))
            # Main folder lookup loop
            for p, e in chain(dpes, ppes):
                folder = OP.join(p, e)
                if not OP.exists(folder):
                    if debuglevel > 1:
                        print('...skipping non-existent folder', folder)
                    continue
                # Suffix lookup loop
                for l, k in product(('', '_FR', '_eng', '_UK', '_esp'), ('', '_ck', '_cl')):
                    pendir = OP.join(folder, pfld_name + l + k)
                    if debuglevel > 1:
                        print(' ... examining ' + pendir + '/' + f)
                    if not OP.exists(OP.join(pendir, f)):
                        continue
                    with AddDllDirectory(pendir):
                        if debuglevel > 0:
                            print(' ... testing ' + pendir + '/' + f)
                        if _import_pendulo():
                            if debuglevel > 0:
                                print(f + ' responding from ' + pendir)
                            del p, e, l
                            break
                        print(ws(f + ' found in ' + pendir + ' but *NOT* responding'))
                else:
                    # Not found with suffixes -> continue main folder lookup
                    continue
                # Found with l & k suffix - break folder loop
                break
            else:
                # Not found
                raise ImportError('Unable to find an adequate ' + f)

    # dll found and API OK: finalise the import
    # with AddDllDirectory(pendir):
    #     mod = _import_ganessa(f, bth, dlls, test=False)
    # context will be closed after call to init.
    to_close = AddDllDirectory(pendir)
    mod = _import_pendulo(test=False)
    return pendir, f, mod, to_close, False
