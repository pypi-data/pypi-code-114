# @Time : 2022/3/7 3:47 PM 
# @Author : SailYang

# 定义作用全局变量
def config_init():
    global _config
    _config = {}


# 获取全局变量
def get_config(k):
    try:
        return _config[k]
    except KeyError:
        return None


# 设置全局变量
def set_config(k, v):
    try:
        _config[k] = v
    except KeyError:
        return None
