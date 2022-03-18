import os
import re
import ctypes
from .types import *
from .cfunc import *
from argparse import ArgumentError


class Trace(object):
    def __init__(self, fname: str) -> None:
        self._RECORD_SIZE   = ctypes.sizeof(RecordFull)
        self._FILE          = self._init_trace_file(fname)
        self._COUNT         = 0

    # 初始化 Trace 文件
    def _init_trace_file(self, fname) -> str:
        f_abs = os.path.abspath(fname)
        assert self._check_trace_file(f_abs)
        return f_abs

    # 检查 Trace 文件
    def _check_trace_file(self, fpath: str) -> bool:
        f_stat = os.stat(fpath)
        record_count = f_stat.st_size // self._RECORD_SIZE
        # try:
        #     assert f_stat.st_size == (self._RECORD_SIZE * record_count)
        #     return True
        # except:
        #     return False
        return True

    # 获取当前 Trace 文件的 Record Count
    @property
    def count(self):
        if self._COUNT:
            return self._COUNT
        self._COUNT = os.stat(self._FILE).st_size // self._RECORD_SIZE
        return self._COUNT

    # 使用过滤器获取 Trace
    def ReadWithFilter(self, reg_eip: str, reg_asm: str, mode: str, buf_len: int=100000) -> PyTraceArray:
        ## 参数检查
        assert isinstance(reg_eip,  str)
        assert isinstance(reg_asm,  str)
        assert isinstance(mode,     str)
        mode = mode.lower()
        assert mode in ('and', 'or')
        assert isinstance(buf_len, int) and buf_len > 0 and buf_len < C_MAX

        ## 参数转换与校验
        c_fname = ctypes.create_string_buffer(self._FILE.encode('UTF-8'))
        try:
            re.compile(reg_eip)
            re.compile(reg_asm)
        except re.error as e:
            raise ArgumentError("正则表达式解析失败: %s", str(e))
        c_reg_eip = ctypes.create_string_buffer(reg_eip.encode('ASCII'))
        c_reg_asm = ctypes.create_string_buffer(reg_asm.encode('ASCII'))
        if ( mode == 'and' ):
            mode = ENUM_FILTER_MODE_AND
        elif ( mode == 'or' ):
            mode = ENUM_FILTER_MODE_OR
        c_buf_len = ctypes.c_int64(buf_len)

        ### 响应体 array 类型定义以及分配
        rf_array_p_type = RecordFull * buf_len
        rf_array = rf_array_p_type()

        ### LIB 函数调用
        count = c_getTraceWithFilter(
            c_fname,
            ctypes.byref(rf_array),
            c_buf_len,
            c_reg_eip,
            c_reg_asm,
            mode
            )
        return PyTraceArray(rf_array, int(count))

    # 根据范围获取trace
    def ReadWithRange(self, rid_start: int, rid_end: int, buf_len: int=10000) -> PyTraceArray:
        assert isinstance(rid_start, int)
        assert isinstance(rid_end, int)
        assert isinstance(buf_len, int)
        assert buf_len > 0
        if rid_start < 0:
            rid_start = self.count + rid_start + 1
        if rid_end < 0:
            rid_end = self.count + rid_end + 1
        assert (0<=rid_start) and (rid_start<rid_end) and (rid_end<=self.count)
        rf_array_p_type = RecordFull * buf_len
        rf_array = rf_array_p_type()
        ret = c_getTraceWithRange(
            ctypes.create_string_buffer(self._FILE.encode('UTF-8')),
            ctypes.byref(rf_array),
            ctypes.c_int64(buf_len),
            ctypes.c_int64(rid_start),
            ctypes.c_int64(rid_end)
        )
        return PyTraceArray(rf_array, int(ret))

    # 读取一行
    def ReadLineWithRid(self, rid: int) -> PyTraceArray:
        assert isinstance(rid, int) and 0 <= rid and rid < self.count
        ret = self.ReadWithRange(rid, rid+1, 1)
        return ret

    # 获取头部数据
    def head(self, count: int=20, show: bool=True):
        assert isinstance(count, int) and count > 0 and count < self.count
        ret = self.ReadWithRange(0, count)
        if show: ret.show()
        return ret
    
    # 获取尾部数据
    def tail(self, count: int=20, show: bool=True):
        assert isinstance(count, int) and count > 0 and count < self.count
        ret = self.ReadWithRange(-count, -1)
        if show: ret.show()
        return ret

    # 获取某个数据的扩展数据
    def extend_up(self, current: int, count: int=20, show: bool=False) -> PyTraceArray:
        assert isinstance(current, int) and current >= 0 and current <= self.count
        assert isinstance(count,   int) and count   >  0
        start  = current - count
        start  = 0 if start < 0 else start
        end    = current
        length = end - start
        ret = self.ReadWithRange(start, end, length)
        if show: ret.show()
        return ret

    def extend_down(self, current, count: int=20, show: bool=False) -> PyTraceArray:
        assert isinstance(current, int) and current >= 0 and current <= self.count
        assert isinstance(count,   int) and count   >  0
        start  = current + 1
        end    = current + count + 1
        end    = self.count if end > self.count else end
        length = end - start
        if start > self.count:
            return PyTraceArray.null()
        ret = self.ReadWithRange(start, end, length)
        if show: ret.show()
        return ret

    def extend(self, current, count: int=20, show: bool=False) -> PyTraceArray:
        ext_u = self.extend_up(current, count, show=False)
        ext_d = self.extend_down(current, count, show=False)
        ext_c = self.ReadLineWithRid(current)
        ret = ext_u + ext_c + ext_d
        if show: ret.show()
        return ret

if __name__ == '__main__':
    print('Hello World!')
