import os
import re

import pandas

from .globals import _VCARD, _TYPE
from .vcard import VcardData


def read_file(fn, ftpye="excel", sheet=0):
    '''
    fn: 文件名；
    return DataFrame
    '''
    assert os.path.isfile(fn), "文件不存在"

    if ftpye == "excel":
        return pandas.read_excel(fn, sheet_name=sheet)
    elif ftpye == "csv":
        return pandas.read_csv(fn, encoding="utf-8")

    return pandas.read_excel(fn, sheet_name=sheet)


def analysis(fn, ftpye=None, sheet=None):
    '''
    fn == 文件名称
    return == 生成器
    '''
    fd = read_file(fn, ftpye, sheet)
    title = fd.columns
    assert (("姓名" in title.array)
            and ("电话" in title.array)), "缺少必要数据\n--help 显示帮助信息"
    for i in fd.index.values:
        data = fd.loc[i, title].to_dict()
        # print(i, data)
        data_tmp = data.copy()
        for tmp in data_tmp:
            assert pandas.notna(data[tmp]), "检查到<{}>有空".format(tmp)
            if not pandas.notna(data[tmp]):
                print("检查到", tmp, "有空")
                del(data[tmp])
        del(data_tmp)
        d = {}
        for k in data:
            key = _VCARD.get(k)
            if key:
                d[key] = VcardData(data[k])
            else:
                _type = None
                for vk in _VCARD:
                    if vk in k:
                        # 通过正则取得括号中的类型
                        types = re.findall(f"[（|()](.*)[)|）]", k)
                        if types and len(types) == 1:
                            _type = _TYPE.get(types[0])
                        key = _VCARD[vk]
                if d.get(key):
                    d[key].append(data[k], _type)
                else:
                    assert type(key)==str, "并不支持这个（{}）字段".format(k)
                    d[key] = VcardData(data[k], _type)
        # print(d)
        yield d
