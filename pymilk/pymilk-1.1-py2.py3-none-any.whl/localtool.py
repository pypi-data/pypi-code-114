import hashlib, re
from datetime import datetime
from math import ceil
from pathlib import Path as libpath
from os.path import abspath
from json import dumps as json_dumps
from json import loads as json_loads
from pickle import dumps as pickle_dumps
from pickle import loads as pickle_loads
from decimal import Decimal
from .data_structures import ungive


# 把路径转化成 /a/b/c.py 的格式
def prepath(path):
    path = abspath(path).replace('\\', '/')
    if path[-1:] == '/':
        return path[:-1]
    else:
        return path

nowdate = lambda : str(datetime.now())[:10]  # -> '2021-10-24'
nowtime = lambda : str(datetime.now())[:19]  # -> '2021-10-24 20:19:10'
pretty_time = lambda : f"[{nowtime()}]"      # -> '[2021-10-24 20:18:57]'

def get_md5(text):
    return hashlib.md5(text.encode(encoding='utf-8')).hexdigest()

def cut_data(data, size):
    return [data[size*(i-1): size*i] for i in range(1, ceil(len(data)/size)+1)]

def set_path(path):
    libpath(path).mkdir(parents=True, exist_ok=True)

def json_chinese(data):
    return json_dumps(data, ensure_ascii=False)

def write_json(fpath, data, ensure_ascii=False):
    data = json_dumps(data, ensure_ascii=ensure_ascii)
    libpath(fpath).write_text(data, encoding='utf8')

def read_json(fpath, default=ungive):
    try:
        return json_loads(libpath(fpath).read_text(encoding='utf8'))
    except Exception as e:
        if default is ungive:
            raise e
        else:
            return default

def write_pickle(fpath, data):
    libpath(fpath).write_bytes(pickle_dumps(data))

def read_pickle(fpath, default=ungive):
    try:
        return pickle_loads(libpath(fpath).read_bytes())
    except Exception as e:
        if default is ungive:
            raise e
        else:
            return default

def limit_input(prompt='', limit=None):
    if type(limit) in (list, tuple, set, dict, str):
        while True:
            user = input(prompt)
            if user in limit: return user
    elif limit is int:
        while True:
            try:
                return int(input(prompt))
            except: pass
    elif limit is float:
        while True:
            try:
                return float(input(prompt))
            except: pass
    else:
        return input(prompt)

# Python的三元表达式
# ternary(O, T, F) 比 T if O else F 可读性更好不是吗?
def ternary(obj, tv, fv):
    return tv if obj else fv

# 把Python对象转化成可被JSON序列化的对象
# 例如：从MySQL数据库提取出来的数据，可能含有Decimal、datetime等数据类型，而这些类型的数据是无法JSON化的。
def can_json(obj, force_key=False, format_time=lambda t: int(t.timestamp())):
    try:
        json_dumps(obj)
        return obj
    except:
        type_ = type(obj)
        if type_ in (list, set, tuple):
            obj = [can_json(x, force_key=force_key, format_time=format_time) for x in obj]
            if type_ in (tuple, ):
                return type_(obj)
            else:
                return obj
        elif type_ is dict:
            newobj = {}
            for k, v in obj.items():
                v = can_json(v, force_key=force_key, format_time=format_time)
                if force_key:
                    k = can_json(k, force_key=force_key, format_time=format_time)
                newobj[k] = v
            return newobj
        elif type_ is Decimal:
            return float(obj)
        elif type_ is datetime:
            return format_time(obj)
        else:
            raise TypeError(f"未知的数据类型: {type_}")

def quick_iter(obj):
    for i, x in enumerate(obj): yield i, x, type(x)
