import os
import stat
import ctypes
import urllib.request
from .types import *

_dll_path = os.path.join(os.path.dirname(__file__), 'bin/rrlib.so')
# print(_dll_path)
# 加载动态链接库
if not os.path.exists(_dll_path):
    print("首次使用, 动态加载链接库中...")
    os.mkdir(os.path.dirname(_dll_path))
    with open(_dll_path, 'wb') as f:
        resp = urllib.request.urlopen('https://cdn.jsdelivr.net/gh/tylzh97/smallfiles/rrlib.so')
        f.write(resp.read())
    os.chmod(_dll_path, stat.S_IRWXU)
TRACE_LIB = ctypes.CDLL(_dll_path)


# 使用 ctypes 加载并初始化动态链接库函数
c_getTraceWithFilter = TRACE_LIB.getTraceWithFilter
c_getTraceWithFilter.argtypes = [
    ctypes.c_char_p,    # Trace 文件路径
    ctypes.c_void_p,    # RecordFull结构体 Buffer 指针
    ctypes.c_int64,     # RecordFull结构体 Buffer 最大长度
    ctypes.c_char_p,    # EIP 寄存器的过滤正则表达式
    ctypes.c_char_p,    # ASM Intel x86汇编过滤的正则表达式
    ctypes.c_int32      # 过滤模式 0: or; 1: and
    ]
c_getTraceWithFilter.restype = ctypes.c_int64 # 响应过滤得到的内容长度

c_getTraceWithRange = TRACE_LIB.getTraceWithRange
c_getTraceWithRange.argtypes = [
    ctypes.c_char_p,
    ctypes.c_void_p,
    ctypes.c_int64,
    ctypes.c_int64,
    ctypes.c_int64,
]
c_getTraceWithRange.restype = ctypes.c_int64
