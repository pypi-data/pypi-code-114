# -*- coding: utf-8 -*-
import ctypes
import time
from datetime import datetime, timedelta
from typing import Optional

import pandas as pd

from yangke.common.config import logger


def ctypes_str2char_array(string: str):
    """
    python3中的字符串是以utf-8格式编码的，为了将字符串传递给C函数，需要将其解码为byte类型，对应C函数中的char*类型或char[]类型

    :param string:
    :return:
    """
    return string.encode("utf8")


class DllMode:
    def __init__(self, ip=None, user=None, passwd_str=None, port=None):
        # self.dll = ctypes.cdll.LoadLibrary(r"D:\lengduan\test2\dbpapi_x64.dll")
        path = r"D:\lengduan\lib4python\yangke\sis\dbpapi_x64.dll"
        try:
            self.handle: Optional[ctypes.c_uint64] = None
            self.dll = ctypes.cdll.LoadLibrary(path)
        except OSError:
            logger.warning(f"找不到指定的动态链接库！请检查路径{path}")
            raise OSError(f"找不到指定的动态链接库！请检查路径{path}")
        if ip is not None and user is not None and passwd_str is not None and port is not None:
            self.connect(ip, user, passwd_str, port)

    def __del__(self):
        self.close()

    def connect(self, ip, user, passwd_str, port):
        self.dll.DBPCreate2.restype = ctypes.c_uint64
        ip = ctypes_str2char_array(ip)
        user = ctypes_str2char_array(user)
        passwd = ctypes_str2char_array(passwd_str)

        self.handle = ctypes.c_uint64(self.dll.DBPCreate2(ip, user, passwd, port, 0))
        if self.handle is None:
            print("连接创建失败")
            return False
        ret = self.dll.DBP_Connect(self.handle)
        if 0 == ret:
            return True
        else:
            print("服务器连接失败")
            return False

    def close(self):
        if self.handle is not None and self.handle.value > 0:
            self.dll.DBP_Close(self.handle)
            self.handle = None

    def is_connect(self):
        ret = self.dll.DBP_IsConnect(self.handle)
        if 0 == ret:
            return True
        return False

    def dis_connect(self):
        """
        断开连接

        :return:
        """
        ret = self.dll.DBP_DisConnect(self.handle)
        if 0 == ret:
            return True
        return False

    def get_his_value(self, tags, start_time: datetime = None, end_time: datetime = None, time_interval=10):
        """
        待验证

        :param tags:
        :param start_time:
        :param end_time:
        :param time_interval: 时间间隔，单位s
        :return:
        """
        n_size = len(tags)
        tag_names = (ctypes.c_char_p * n_size)()  # 名字
        for i in range(n_size):
            tag_names[i] = ctypes_str2char_array(tags[i])

        start_time = start_time or datetime.now() - timedelta(days=1, hours=2)  # 默认两小时前的时间为读数起始时间
        end_time = end_time or datetime.now() - timedelta(days=1, hours=1)  # 默认一小时前的时间为读数结束时间
        start_time_long = int(time.mktime(start_time.timetuple()))  # 将时间转为UNIX时间
        end_time_long = int(time.mktime(end_time.timetuple()))
        start_time_c = ctypes.c_long(start_time_long)  #
        end_time_c = ctypes.c_long(end_time_long)
        flag = ctypes.c_long(3)  # 标记，不知道什么意思
        data_size = (end_time_long - start_time_long) // time_interval
        time_interval = ctypes.c_long(time_interval)
        value_double_arr = (ctypes.c_double * data_size)()
        value2_arr = (ctypes.c_int32 * data_size)()
        time_long_arr = (ctypes.c_uint32 * data_size)()
        qas_short_arr = (ctypes.c_short * data_size)()
        value2_type = (ctypes.c_int32 * data_size)()  # 数据类型
        data_size_arr = (ctypes.c_int32 * data_size)()
        self.dll.DBPGetHisVal(self.handle,
                              tag_names,
                              start_time_c,
                              end_time_c,
                              time_interval,
                              flag,
                              value_double_arr,
                              value2_arr,
                              time_long_arr,
                              qas_short_arr,
                              n_size,
                              value2_type,
                              data_size_arr
                              )
        print(data_size_arr)

    def get_snapshot(self, tags, tag_description=None, need_detail=False, use_description=True):
        """
        获取给定标签列表的快照数据

        :param tags: 标签名
        :param need_detail:是否需要数据的详细信息，默认不需要，如果为True,则会返回数据质量、错误码等详细信息
        :param tag_description: 标签点的描述
        :param use_description: 当给定点描述时，数据列的标题是否使用点描述代替标签名
        :return:
        """

        n_size = len(tags)
        tag_names = (ctypes.c_char_p * n_size)()  # 名字
        for i in range(n_size):
            tag_names[i] = ctypes_str2char_array(tags[i])

        time_long_arr = (ctypes.c_uint32 * n_size)()  # 时间
        qas_short_arr = (ctypes.c_short * n_size)()  # 质量

        value_double_arr = (ctypes.c_double * n_size)()  # 浮点数类型的值
        value2_arr = (ctypes.c_int32 * n_size)()  # 整形类型的值
        value2_type = (ctypes.c_int32 * n_size)()  # 数据类型
        error_code_arr = (ctypes.c_short * n_size)()  # 数据错误码
        self.dll.DBPGetSnapshot(
            self.handle,  # 句柄
            tag_names,  # char* sTagNames[],  //in,标签名字符串指针数组  //apistring
            time_long_arr,  # long ltimes[],   //in, 时标
            qas_short_arr,  # short snqas[],   //in, 质量
            value_double_arr,  # double  dblvals[],   //in, 存放double值,DT_FLOAT32,DT_FLOAT64存放区
            value2_arr,  # long lvals[],   //in, 存放Long值,DT_DIGITAL,DT_INT32,DT_INT64存放区
            value2_type,  # int  ntypes[],   //in, 数据类型,DT_INT32,DT_FLOAT32等。
            error_code_arr,  # short errs[],    //in/out, 错误码
            n_size  # int  nsize    //in, 个数
        )
        if tag_description is not None and use_description:  # 如果使用描述，且描述不为空
            return self._assemble_dataframe(tag_description, time_long_arr,
                                            qas_short_arr, value_double_arr, value2_arr,
                                            value2_type,
                                            error_code_arr, need_detail=need_detail)
        else:
            return self._assemble_dataframe(tags, time_long_arr, qas_short_arr,
                                            value_double_arr, value2_arr,
                                            value2_type,
                                            error_code_arr, need_detail=need_detail)

    @staticmethod
    def _assemble_dataframe(tags, time_long_arr, qas_short_arr, value_double_arr, value2_arr, value2_type,
                            error_code_arr, need_detail=False):
        """
        将代理服务器返回的数据组装成dataframe格式的对象

        :param tags: 数据标签
        :param time_long_arr:
        :param qas_short_arr:
        :param value_double_arr:
        :param value2_arr:
        :param value2_type:
        :param error_code_arr:
        :param need_detail: 是否需要数据的详细信息，默认不需要，如果为True,则会返回数据质量、错误码等详细信息
        :return:
        """
        n_size = len(time_long_arr)  # 标签个数
        if not need_detail:
            columns = ["DateTime"]
            columns.extend(tags)
            time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time_long_arr[0]))
            data_list = [time_str]
            for i in range(n_size):
                if value2_type[i] == 3:  # 如果数据类型==3，则说明读到的是double类型数据
                    data_list.append(value_double_arr[i])
                else:
                    data_list.append(value2_arr[i])
            result = pd.DataFrame(columns=columns, data=[data_list])
        else:
            result = {}
            for i in range(n_size):
                tag = tags[i]
                columns = ["DateTime", "值", "质量", "数据类型", "错误码"]
                time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time_long_arr[i]))
                qas = qas_short_arr[i]
                value_type = value2_type[i]
                if value_type == 3:
                    value = value_double_arr[i]
                else:
                    value = value2_arr[i]
                error_code = error_code_arr[i]
                data_list = [time_str, value, qas, value_type, error_code]
                dataframe = pd.DataFrame(columns=columns, data=[data_list])
                result.update({tag: dataframe})
        return result

    def write_snapshot_double(self, tags, values):
        """
        写double类型数据到数据库

        :param tags: 标签名列表
        :param values: 数值列表
        :return:
        """
        n_size = len(tags)
        tag_names = (ctypes.c_char_p * n_size)()  # 名字
        time_long_arr = (ctypes.c_uint32 * n_size)()  # 时间
        qas_short_array = (ctypes.c_short * n_size)()  # 质量
        value_double_arr = (ctypes.c_double * n_size)()  # 浮点数类型的值
        value2_arr = (ctypes.c_int32 * n_size)()  # 整形类型的值
        value_type = (ctypes.c_int32 * n_size)()  # 数据类型
        time_long = int(time.time())  # 保证写入的数据点都具有同一个时标
        for i in range(n_size):
            tag_names[i] = ctypes_str2char_array(tags[i])
            time_long_arr[i] = time_long
            qas_short_array[i] = 0
            value_double_arr[i] = values[i]
            value2_arr[i] = 0
            value_type[i] = 3  # 3表示通过value_double_arr传输数据，其他表示通过value2_arr传输数据

        error_code_arr = (ctypes.c_short * 2)()  # 数据错误码，输出信息

        self.dll.DBPWriteSnapshot(
            self.handle,  # 句柄
            tag_names,  # char* sTagNames[],  //in,标签名字符串指针数组  //apistring
            time_long_arr,  # long ltimes[],   //in, 时标
            qas_short_array,  # short snqas[],   //in, 质量
            value_double_arr,  # double  dblvals[],   //in, 存放double值,DT_FLOAT32,DT_FLOAT64存放区
            value2_arr,  # long lvals[],   //in, 存放Long值,DT_DIGITAL,DT_INT32,DT_INT64存放区
            value_type,  # int  ntypes[],   //in, 数据类型,DT_INT32,DT_FLOAT32等。
            error_code_arr,  # short errs[],    //in/out, 错误码
            n_size  # int  nsize    //in, 个数
        )
