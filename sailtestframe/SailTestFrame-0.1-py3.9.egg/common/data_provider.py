# @Time : 2022/3/6 5:45 PM 
# @Author : SailYang
import re


def data_provider(test_data):
    """
    给测试用例加上"__data_Provider__"属性，供测试用例查找时能调用（装饰在test_demo_data_driven测试方式上）
    """

    def wrapper(func):
        # 给测试用例增加一个__data_Provider__属性
        setattr(func, "__data_Provider__", test_data)

        # 计算测试数据的组数，在生成新测试用例的时候使用
        global index_len
        index_len = len(str(len(test_data)))
        return func

    return wrapper


def mk_test_name(name, value, index=0):
    """
    用于根据测试数据的组数，分组并生成新的测试用名字
    """

    # 通过index_len的长度使测试用例名称保持一致风格，00001
    index = "{0:0{1}d}".format(index + 1, index_len)
    test_name = f"{name}_{index}_{str(value)}"

    # 将测试数据中的非法字符替换成 "_"，以生成新的测试用例名
    return re.sub(r'\W|^(?=\d)', '_', test_name)
