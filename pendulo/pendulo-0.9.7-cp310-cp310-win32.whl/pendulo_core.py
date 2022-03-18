# -*- coding: utf-8 -*-
'''package interface for Pendulo Penwin32.dll API '''
import re
from typing import List, Sequence, Tuple, Callable, AnyStr
import atexit
import numpy as np

from pendulo._getdll import _getdllinfo

VectF = List[float]

# lookup for a matching folder, dll and import it
_dll_dir, _dll_name, _dll_api, _dll_context, _dll_from_embed = _getdllinfo()

if not _dll_api:
    raise ImportError(f'DLL {_dll_name}: not found or too old.\n')

# get the lang and the protection mode from the folder name
_m = re.search(r'(?:pendulo)_?(fr|fra|eng|esp|sp|uk|us)_?(ck)?\Z',
               _dll_dir, re.IGNORECASE)
_lang, _protmode = _m.group(1, 2) if _m else (None, None)
if not _lang:
    _lang = 'FR'
if not _protmode:
    _protmode = 'Flex?'
# print('Lang is:', _lang, ' * prot is:', _protmode)

loadmodel : Callable[[str], None] = _dll_api.loadmodel
# get_unit_info : Callable[[str], Tuple[float, str, str]] = _dll_api.get_unit_info
get_node : Callable[[str], Tuple[int, float, float, float]] = _dll_api.get_node
set_col_node : Callable[[str, str, VectF, VectF, int], bool] = _dll_api.set_col_node
size_TS : Callable[[str, str, str], int] = _dll_api.size_ts
result_TS : Callable[[int], Tuple[VectF, VectF]] = _dll_api.result_ts

def u(input_str: AnyStr) -> str:
    '''Converts to unicode - cp1252 first guess'''
    if isinstance(input_str, str):
        return input_str
    if isinstance(input_str, bytes):
        for codec in ('cp1252', 'utf-8', 'cp850', 'iso-8859-1'):
            try:
                return str(input_str, codec)
            except UnicodeError:
                continue
    else:
        return str(input_str)


def init(debug : int = 0) -> str:
    '''kernel initialisation - debug=0 for silent use, 1 or 2 for verbose'''
    return _dll_api.init(debug)

def close() -> str:
    '''ends the session'''
    global _dll_api, _dll_dir
    _dll_context.close()
    if _dll_dir:
        try:
            text = 'pendulo unloaded.'
            _dll_api.quit()
            # _dll_version = 0
            del _dll_api
        except NameError:
            text = 'pendulo already unloaded...'
        _dll_dir = ''
    else:
        text = 'pendulo was not loaded!'
    print(text)
    return text
# Register closepic function for proper exit
atexit.register(close)
quit = close

def get_unit_info(attr : str) -> Tuple[float, str, str]:
    '''Returns unit coef, name and reference unit'''
    coef, name, ref_name =_dll_api.get_unit_info(attr)
    return coef, u(name), u(ref_name)

def set_node_boundary_condition(node : str, ts_data : Sequence[Tuple[float, float]], cond='CS') -> bool:
    '''Sets a boundary condition (CS or CH or P) on a node
    ts_data is a sequence of tuples (time, value)'''
    nb_val = len(ts_data)
    times, values = zip(*ts_data)
    return set_col_node(node, cond, np.asfortranarray(times, dtype=np.float32),
                                    np.asfortranarray(values, dtype=np.float32), nb_val)

def run_simulation(horizon : float = -1, storage_factor : float = -1) -> bool:
    '''Runs the simulation - if parameters are not provided, use model's'''
    return _dll_api.run_simulation(horizon, storage_factor)

def ts(id_elem : str, typelt : str = 'NODE', attr : str = 'CH') -> Tuple[VectF, VectF]:
    '''Gets result TS from element id_elem - default CH (head) from NODE'''
    # Map UK attr to French
    attr = dict(HH='CH').get(attr, attr)
    # Build internal lookup info and return arrays lenght for caller
    nbval = size_TS(typelt, id_elem, attr)
    # retrieve time and value arrays from last element and attr called
    if nbval:
        return result_TS(nbval)
    return [], []
